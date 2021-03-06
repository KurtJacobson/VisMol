#!/usr/bin/env python

import math
import numpy as np
import ctypes
import camera as cam

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

import OpenGL
from OpenGL import GL
from OpenGL.GL import shaders

global degrees
degrees = np.float32(0)

class MyGLProgram():
    def __init__(self, vertex, fragment):
        self.glarea = Gtk.GLArea.new()
        self.glarea.connect("realize", self.initialize)
        self.glarea.connect("render", self.render)
        self.vertex_shader = vertex
        self.fragment_shader = fragment
        self.model_mat = self.view_mat = self.proj_mat = np.identity(4, dtype=np.float32)
        
    def initialize(self, otro):
        self.glarea.set_has_depth_buffer(True)
        self.glarea.set_has_alpha(True)
        self.flag = True
    
    def load_shaders(self):
        my_vertex = GL.glCreateShader(GL.GL_VERTEX_SHADER)
        GL.glShaderSource(my_vertex, self.vertex_shader)
        GL.glCompileShader(my_vertex)
        my_fragment = GL.glCreateShader(GL.GL_FRAGMENT_SHADER)
        GL.glShaderSource(my_fragment, self.fragment_shader)
        GL.glCompileShader(my_fragment)
        self.program = GL.glCreateProgram()
        GL.glAttachShader(self.program, my_vertex)
        GL.glAttachShader(self.program, my_fragment)
        GL.glLinkProgram(self.program)
        self.load_data()
        self.flag = False
        
        #my_vertex = shaders.compileShader(self.vertex_shader, GL.GL_VERTEX_SHADER)
        #my_fragment = shaders.compileShader(self.fragment_shader, GL.GL_FRAGMENT_SHADER)
        ##print my_vertex
        #self.program = shaders.compileProgram(my_vertex, my_fragment)
        ##print self.program, '<-- init'
        ##self.vertex_array_object = self.load_data()
        #self.load_data()
        #self.flag = False
        ##print self.vertex_array_object, 'VAO'
    
    def render(self, area, context):
        if self.flag:
            self.load_shaders()
        GL.glClearColor(0.0, 0.0, 0.0, 1.0)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        #print self.program, 'rendereing'
        GL.glUseProgram(self.program)
        
        global degrees
        model = view = proj = np.identity(4, dtype=np.float32)
        model = cam.my_glRotateYf(model, degrees)
        view = cam.my_glTranslatef(view, np.array([0,0,-3],dtype=np.float32))
        aloc = self.glarea.get_allocation()
        w = np.float32(aloc.width)
        h = np.float32(aloc.height)
        proj = cam.my_gluPerspectivef(proj, 30, w/h, 0.1, 10.0)
        
        self.model = GL.glGetUniformLocation(self.program, 'model_mat')
        GL.glUniformMatrix4fv(self.model, 1, GL.GL_FALSE, model)
        self.view = GL.glGetUniformLocation(self.program, 'view_mat')
        GL.glUniformMatrix4fv(self.view, 1, GL.GL_FALSE, view)
        self.proj = GL.glGetUniformLocation(self.program, 'projection_mat')
        GL.glUniformMatrix4fv(self.proj, 1, GL.GL_FALSE, proj)
        
        GL.glBindVertexArray(self.vertex_array_object)
        if self.coords is None:
            pass
        else:
            GL.glDrawArrays(GL.GL_LINES, 0, len(self.coords))
        
        GL.glBindVertexArray(0)
        GL.glUseProgram(0)
        degrees += 1
        if degrees >= 360:
            degrees = np.float32(0)
    
    def load_data(self):
        self.vertex_array_object = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vertex_array_object)
        vertex_buffer_object = GL.glGenBuffers(1)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, vertex_buffer_object)
        self.coords = np.array([ 0.0, 1.0, 0.0,  1.0, 0.0, 0.0,
                                 1.0,-1.0,-1.0,  1.0, 0.0, 0.0,
                                 1.0,-1.0, 1.0,  1.0, 0.0, 0.0,
                                 0.0, 1.0, 0.0,  0.0, 1.0, 0.0,
                                 1.0,-1.0,-1.0,  0.0, 1.0, 0.0,
                                -1.0,-1.0,-1.0,  0.0, 1.0, 0.0,
                                 0.0, 1.0, 0.0,  0.0, 0.0, 1.0,
                                -1.0,-1.0,-1.0,  0.0, 0.0, 1.0,
                                -1.0,-1.0, 1.0,  0.0, 0.0, 1.0,
                                 0.0, 1.0, 0.0,  1.0, 0.0, 1.0,
                                -1.0,-1.0, 1.0,  1.0, 0.0, 1.0,
                                 1.0,-1.0, 1.0,  1.0, 0.0, 1.0,
                                -1.0,-1.0, 1.0,  1.0, 1.0, 0.0,
                                -1.0,-1.0,-1.0,  1.0, 1.0, 0.0,
                                 1.0,-1.0,-1.0,  1.0, 1.0, 0.0,
                                -1.0,-1.0, 1.0,  0.0, 1.0, 1.0,
                                 1.0,-1.0, 1.0,  0.0, 1.0, 1.0,
                                 1.0,-1.0,-1.0,  0.0, 1.0, 1.0], dtype=np.float32)
        GL.glBufferData(GL.GL_ARRAY_BUFFER, self.coords.itemsize*len(self.coords), self.coords, GL.GL_STATIC_DRAW)
        
        position = GL.glGetAttribLocation(self.program, 'coordinate')
        GL.glEnableVertexAttribArray(position)
        gl_colors = GL.glGetAttribLocation(self.program, 'my_color')
        GL.glEnableVertexAttribArray(gl_colors)
        GL.glVertexAttribPointer(position, 3, GL.GL_FLOAT, GL.GL_FALSE, 6*self.coords.itemsize, ctypes.c_void_p(0))
        GL.glVertexAttribPointer(gl_colors, 3, GL.GL_FLOAT, GL.GL_FALSE, 6*self.coords.itemsize, ctypes.c_void_p(3*self.coords.itemsize))
        GL.glBindVertexArray(0)
         
        GL.glDisableVertexAttribArray(position)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, 0)




vertex_shader = """
#version 330

uniform mat4 model_mat;
uniform mat4 view_mat;
uniform mat4 projection_mat;

in vec3 coordinate;
in vec3 my_color;

out vec3 sh_color;

void main()
{
   sh_color = my_color;
   //gl_Position = vec4(coordinate, 1.0);
   //gl_Position = camera * vec4(coordinate, 1);
   gl_Position = projection_mat * view_mat * model_mat * vec4(coordinate, 1);
}
"""
 
fragment_shader = """
#version 330

in vec3 sh_color;

out vec4 final_color;

void main()
{
   final_color = vec4(sh_color, 1.0);
}
"""

test = MyGLProgram(vertex_shader, fragment_shader)
wind = Gtk.Window()
wind.add(test.glarea)

wind.connect("delete-event", Gtk.main_quit)
wind.show_all()
Gtk.main()





























