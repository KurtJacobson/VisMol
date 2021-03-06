#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  camera.py
#  
#  Copyright 2016 Labio <labio@labio-XPS-8300>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import math
import numpy as np
import ctypes


def my_gluLookAt(in_matrix, eye, target, up):
    forward = target - eye
    forward = forward/np.linalg.norm(forward)
    side = np.cross(forward, up)
    side = side/np.linalg.norm(side)
    up = np.cross(side, forward)
    temp_matrix = np.identity(4, dtype=np.float32)
    temp_matrix[:3,0] = side
    temp_matrix[:3,1] = up
    temp_matrix[:3,2] = -forward
    #result_matrix = my_glMultiplyMatricesf(in_matrix, temp_matrix)
    #result_matrix = my_glTranslatef(result_matrix, -eye)
    result_matrix = my_glTranslatef(temp_matrix, -eye)
    return result_matrix
    #view_matrix = np.identity(4, dtype=np.float32)
    #forward = target - eye
    #forward = forward/np.linalg.norm(forward)
    #side = np.cross(up, forward)
    #side = side/np.linalg.norm(side)
    #up = np.cross(forward, side)
    #up = up/np.linalg.norm(up)
    #dot_x = -np.dot(side, eye)
    #dot_y = -np.dot(up, eye)
    #dot_z = -np.dot(forward, eye)
    #view_matrix[:3,0] = side
    #view_matrix[:3,1] = up
    #view_matrix[:3,2] = -forward
    #view_matrix[3,0] = dot_x
    #view_matrix[3,1] = dot_y
    #view_matrix[3,2] = dot_z
    #return view_matrix

def my_gluPerspectived(fovy, aspect, z_near, z_far):
    y_max = np.float64(z_near*math.tan(fovy*math.pi/360.0))
    x_max = np.float64(y_max*aspect)
    return my_gluFrustumd(-x_max, x_max, -y_max, y_max, z_near, z_far)

def my_gluFrustumd(left, rigth, bottom, top, near, far):
    frust = np.zeros((4,4), dtype=np.float64)
    frust[0,0] = np.float64((2*near)/(rigth-left))
    frust[1,1] = np.float64((2*near)/(top-bottom))
    frust[2,0] = np.float64((rigth+left)/(rigth-left))
    frust[2,1] = np.float64((top+bottom)/(top-bottom))
    frust[2,2] = np.float64((-far-near)/(far-near))
    frust[2,3] = np.float64(-1)
    frust[3,2] = np.float64((-2*near*far)/(far-near))
    return frust

def my_gluFrustumf(left, rigth, bottom, top, near, far):
    frust = np.zeros((4,4), dtype=np.float32)
    frust[0,0] = np.float32((2*near)/(rigth-left))
    frust[1,1] = np.float32((2*near)/(top-bottom))
    frust[2,0] = np.float32((rigth+left)/(rigth-left))
    frust[2,1] = np.float32((top+bottom)/(top-bottom))
    frust[2,2] = np.float32((-far-near)/(far-near))
    frust[2,3] = np.float32(-1)
    frust[3,2] = np.float32((-2*near*far)/(far-near))
    return frust

def my_glRotateXf(in_matrix, angle):
    angle = angle*math.pi/180.0
    rot_matrix = np.identity(4, dtype=np.float32)
    rot_matrix[1,1] = math.cos(angle)
    rot_matrix[2,1] = math.sin(angle)
    rot_matrix[1,2] = -math.sin(angle)
    rot_matrix[2,2] =  math.cos(angle)
    return my_glMultiplyMatricesf(in_matrix, rot_matrix)

def my_glRotateYf(in_matrix, angle):
    angle = angle*math.pi/180.0
    rot_matrix = np.identity(4, dtype=np.float32)
    rot_matrix[0,0] = math.cos(angle)
    rot_matrix[0,2] = math.sin(angle)
    rot_matrix[2,0] = -math.sin(angle)
    rot_matrix[2,2] =  math.cos(angle)
    return my_glMultiplyMatricesf(in_matrix, rot_matrix)

def my_glRotateZf(in_matrix, angle):
    angle = angle*math.pi/180.0
    rot_matrix = np.identity(4, dtype=np.float32)
    rot_matrix[0,0] = math.cos(angle)
    rot_matrix[1,0] = math.sin(angle)
    rot_matrix[0,1] = -math.sin(angle)
    rot_matrix[1,1] =  math.cos(angle)
    return my_glMultiplyMatricesf(in_matrix, rot_matrix)


#################### FUNCIONANDO ####################


def my_glScalef(in_matrix, x_scale, y_scale, z_scale):
    x_scale = np.float32(x_scale)
    y_scale = np.float32(y_scale)
    z_scale = np.float32(z_scale)
    scale_matrix = np.identity(4, dtype=np.float32)
    scale_matrix[0,0] = x_scale
    scale_matrix[1,1] = y_scale
    scale_matrix[2,2] = z_scale
    return my_glMultiplyMatricesf(in_matrix, scale_matrix)

def my_glTranslatef(orig_matrix, position):
    trans_matrix = np.identity(4, dtype=np.float32)
    #trans_matrix[:3,3] = position
    trans_matrix[3,:3] = position
    return my_glMultiplyMatricesf(orig_matrix, trans_matrix)

def my_glMultiplyMatricesf(mat1, mat2):
    result = np.zeros((4,4), dtype=np.float32)
    result[0,0] = mat1[0,0]*mat2[0,0]+mat1[0,1]*mat2[1,0]+mat1[0,2]*mat2[2,0]+mat1[0,3]*mat2[3,0]
    result[1,0] = mat1[1,0]*mat2[0,0]+mat1[1,1]*mat2[1,0]+mat1[1,2]*mat2[2,0]+mat1[1,3]*mat2[3,0]
    result[2,0] = mat1[2,0]*mat2[0,0]+mat1[2,1]*mat2[1,0]+mat1[2,2]*mat2[2,0]+mat1[2,3]*mat2[3,0]
    result[3,0] = mat1[3,0]*mat2[0,0]+mat1[3,1]*mat2[1,0]+mat1[3,2]*mat2[2,0]+mat1[3,3]*mat2[3,0]
    
    result[0,1] = mat1[0,0]*mat2[0,1]+mat1[0,1]*mat2[1,1]+mat1[0,2]*mat2[2,1]+mat1[0,3]*mat2[3,1]
    result[1,1] = mat1[1,0]*mat2[0,1]+mat1[1,1]*mat2[1,1]+mat1[1,2]*mat2[2,1]+mat1[1,3]*mat2[3,1]
    result[2,1] = mat1[2,0]*mat2[0,1]+mat1[2,1]*mat2[1,1]+mat1[2,2]*mat2[2,1]+mat1[2,3]*mat2[3,1]
    result[3,1] = mat1[3,0]*mat2[0,1]+mat1[3,1]*mat2[1,1]+mat1[3,2]*mat2[2,1]+mat1[3,3]*mat2[3,1]
    
    result[0,2] = mat1[0,0]*mat2[0,2]+mat1[0,1]*mat2[1,2]+mat1[0,2]*mat2[2,2]+mat1[0,3]*mat2[3,2]
    result[1,2] = mat1[1,0]*mat2[0,2]+mat1[1,1]*mat2[1,2]+mat1[1,2]*mat2[2,2]+mat1[1,3]*mat2[3,2]
    result[2,2] = mat1[2,0]*mat2[0,2]+mat1[2,1]*mat2[1,2]+mat1[2,2]*mat2[2,2]+mat1[2,3]*mat2[3,2]
    result[3,2] = mat1[3,0]*mat2[0,2]+mat1[3,1]*mat2[1,2]+mat1[3,2]*mat2[2,2]+mat1[3,3]*mat2[3,2]
    
    result[0,3] = mat1[0,0]*mat2[0,3]+mat1[0,1]*mat2[1,3]+mat1[0,2]*mat2[2,3]+mat1[0,3]*mat2[3,3]
    result[1,3] = mat1[1,0]*mat2[0,3]+mat1[1,1]*mat2[1,3]+mat1[1,2]*mat2[2,3]+mat1[1,3]*mat2[3,3]
    result[2,3] = mat1[2,0]*mat2[0,3]+mat1[2,1]*mat2[1,3]+mat1[2,2]*mat2[2,3]+mat1[2,3]*mat2[3,3]
    result[3,3] = mat1[3,0]*mat2[0,3]+mat1[3,1]*mat2[1,3]+mat1[3,2]*mat2[2,3]+mat1[3,3]*mat2[3,3]
    return result

def my_glRotatef(in_matrix, angle, x, y, z):
    angle = angle*math.pi/180.0
    vector = np.array([x,y,z], dtype=np.float32)
    vector = vector/np.linalg.norm(vector)
    x,y,z = vector
    c = math.cos(angle)
    s = math.sin(angle)
    rot_matrix = np.identity(4, dtype=np.float32)
    rot_matrix[0,0] = x*x*(1-c)+c
    rot_matrix[1,0] = y*x*(1-c)+z*s
    rot_matrix[2,0] = x*z*(1-c)-y*s
    rot_matrix[0,1] = x*y*(1-c)-z*s
    rot_matrix[1,1] = y*y*(1-c)+c
    rot_matrix[2,1] = y*z*(1-c)+x*s
    rot_matrix[0,2] = x*z*(1-c)+y*s
    rot_matrix[1,2] = y*z*(1-c)-x*s
    rot_matrix[2,2] = z*z*(1-c)+c
    return my_glMultiplyMatricesf(in_matrix, rot_matrix)

def my_gluPerspectivef(in_matrix, fovy, aspect, z_near, z_far):
    assert(aspect>0)
    assert(z_far>z_near)
    f = np.float32(1/(math.tan(fovy*math.pi/180.0)))
    pers_matrix = np.zeros((4,4), dtype=np.float32)
    pers_matrix[0,0] = f/aspect
    pers_matrix[1,1] = f
    pers_matrix[2,2] = (z_near+z_far)/(z_near-z_far)
    pers_matrix[3,2] = 2*z_near*z_far/(z_near-z_far)
    pers_matrix[2,3] = -1
    return my_glMultiplyMatricesf(in_matrix, pers_matrix)
    
