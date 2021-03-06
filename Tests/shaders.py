#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  shaders.py
#  
#  Copyright 2017 Carlos Eduardo Sequeiros Borja <casebor@gmail.com>
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

v_shader_dots = """
#version 330

uniform mat4 model_mat;
uniform mat4 view_mat;
uniform mat4 proj_mat;

in vec3 vert_coord;
in vec3 vert_color;

out vec3 frag_color;

void main(){
    frag_color = vert_color;
    gl_Position = proj_mat * view_mat * model_mat * vec4(vert_coord, 1.0);
}
"""
f_shader_dots = """
#version 330

in vec3 frag_color;

out vec4 final_color;

void main(){
    final_color = vec4(frag_color, 1.0);
}
"""

v_shader_diamonds = """
#version 330

uniform mat4 model_mat;
uniform mat4 view_mat;
uniform mat4 proj_mat;

in vec3 vert_coord;
in vec3 vert_color;

out vec4 geom_coord;
out vec3 geom_color;

void main(){
    geom_color = vert_color;
    geom_coord = view_mat * model_mat * vec4(vert_coord, 1);
    //geom_coord = proj_mat * view_mat * model_mat * vec4(vert_coord, 1);
    //gl_Position = vec4(vert_coord, 1.0);
}
"""
g_shader_diamonds = """
#version 330

layout (points) in; // Name for use is gl_in[] is default for GLSL
layout (triangle_strip, max_vertices = 14) out;

uniform mat4 proj_mat;

in vec4 geom_coord[];
in vec3 geom_color[];

out vec3 frag_color;

void main(){
    vec4 offset = vec4(0.0, 0.5, 0.0, 1.0);
    vec4 vertPos = offset + geom_coord[0];
    gl_Position = proj_mat * vertPos;
    frag_color = geom_color[0];
    EmitVertex();
    offset = vec4(-.5, 0.0, 0.0, 1.0);
    vertPos = offset + geom_coord[0];
    gl_Position = proj_mat * vertPos;
    frag_color = geom_color[0];
    EmitVertex();
    offset = vec4(0.0, 0.0, 0.5, 1.0);
    vertPos = offset + geom_coord[0];
    gl_Position = proj_mat * vertPos;
    frag_color = geom_color[0];
    EmitVertex();
    offset = vec4(0.0,-0.5, 0.0, 1.0);
    vertPos = offset + geom_coord[0];
    gl_Position = proj_mat * vertPos;
    frag_color = geom_color[0];
    EmitVertex();
    offset = vec4(0.5, 0.0, 0.0, 1.0);
    vertPos = offset + geom_coord[0];
    gl_Position = proj_mat * vertPos;
    frag_color = geom_color[0];
    EmitVertex();
    offset = vec4(0.0, 0.0,-0.5, 1.0);
    vertPos = offset + geom_coord[0];
    gl_Position = proj_mat * vertPos;
    frag_color = geom_color[0];
    EmitVertex();
    offset = vec4(0.0, 0.5, 0.0, 1.0);
    vertPos = offset + geom_coord[0];
    gl_Position = proj_mat * vertPos;
    frag_color = geom_color[0];
    EmitVertex();
    offset = vec4(-.5, 0.0, 0.0, 1.0);
    vertPos = offset + geom_coord[0];
    gl_Position = proj_mat * vertPos;
    frag_color = geom_color[0];
    EmitVertex();
    EndPrimitive();
    
    offset = vec4(-.5, 0.0, 0.0, 1.0);
    vertPos = offset + geom_coord[0];
    gl_Position = proj_mat * vertPos;
    frag_color = geom_color[0];
    EmitVertex();
    offset = vec4(0.0, 0.0,-0.5, 1.0);
    vertPos = offset + geom_coord[0];
    gl_Position = proj_mat * vertPos;
    frag_color = geom_color[0];
    EmitVertex();
    offset = vec4(0.0,-0.5, 0.0, 1.0);
    vertPos = offset + geom_coord[0];
    gl_Position = proj_mat * vertPos;
    frag_color = geom_color[0];
    EmitVertex();
    EndPrimitive();
    
    offset = vec4(0.0, 0.5, 0.0, 1.0);
    vertPos = offset + geom_coord[0];
    gl_Position = proj_mat * vertPos;
    frag_color = geom_color[0];
    EmitVertex();
    offset = vec4(0.0, 0.0, 0.5, 1.0);
    vertPos = offset + geom_coord[0];
    gl_Position = proj_mat * vertPos;
    frag_color = geom_color[0];
    EmitVertex();
    offset = vec4(0.5, 0.0, 0.0, 1.0);
    vertPos = offset + geom_coord[0];
    gl_Position = proj_mat * vertPos;
    frag_color = geom_color[0];
    EmitVertex();
    EndPrimitive();
}
"""
f_shader_diamonds = """
#version 330

in vec3 frag_color;

out vec4 final_color;

void main(){
    final_color = vec4(frag_color, 1.0);
}
"""

v_shader_circles = """
#version 330

uniform mat4 model_mat;
uniform mat4 view_mat;
uniform mat4 proj_mat;

in vec3 vert_coord;
in vec3 vert_color;

out vec3 frag_color;

void main(){
    frag_color = vert_color;
    gl_Position = proj_mat * view_mat * model_mat * vec4(vert_coord, 1.0);
    gl_PointSize = 50;
}
"""
f_shader_circles = """
#version 330

in vec3 frag_color;

out vec4 final_color;

void main(){
    float dist = length(gl_PointCoord - vec2(0.5, 0.5));
    if (dist > 0.5)
        discard;
    float ligth_dist = length(gl_PointCoord - vec2(0.3, 0.3));
    final_color = mix(vec4(frag_color, 1), vec4(0, 0, 0, 1), sqrt(ligth_dist)*.78);
}
"""

v_shader_lines = """
#version 330

uniform mat4 model_mat;
uniform mat4 view_mat;
uniform mat4 proj_mat;

in vec3 vert_coord;
in vec3 vert_color;

out vec4 geom_coord;
out vec3 geom_color;

void main(){
    geom_color = vert_color;
    geom_coord = view_mat * model_mat * vec4(vert_coord, 1);
}
"""
g_shader_lines = """
#version 330

layout (lines) in;
layout (line_strip, max_vertices = 4) out;

uniform mat4 proj_mat;

in vec4 geom_coord[];
in vec3 geom_color[];

out vec3 frag_color;

void main(){
    vec4 midPoint = (geom_coord[0] + geom_coord[1])/2;
    gl_Position = proj_mat * geom_coord[0];
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * midPoint;
    frag_color = geom_color[0];
    EmitVertex();
    EndPrimitive();
    
    gl_Position = proj_mat * midPoint;
    frag_color = geom_color[1];
    EmitVertex();
    gl_Position = proj_mat * geom_coord[1];
    frag_color = geom_color[1];
    EmitVertex();
    EndPrimitive();
}
"""
f_shader_lines = """
#version 330

in vec3 frag_color;

out vec4 final_color;

void main(){
    float dist = gl_FragCoord.y - 0.5;
    if (dist<0)
        discard;
    final_color = vec4(frag_color, 1);
}
"""

v_shader_antialias = """
#version 330

uniform mat4 model_mat;
uniform mat4 view_mat;
uniform mat4 proj_mat;

in vec3 vert_coord;
in vec3 vert_color;

out vec4 geom_coord;
out vec3 geom_color;

void main(){
    geom_color = vert_color;
    geom_coord = view_mat * model_mat * vec4(vert_coord, 1);
}
"""
g_shader_antialias = """
#version 330

layout (lines) in;
layout (triangle_strip, max_vertices = 20) out;

uniform mat4 proj_mat;
uniform float antialias_length;
uniform vec3 alias_color;

in vec4 geom_coord[];
in vec3 geom_color[];

varying vec4 point_a[4];
varying vec4 point_b[4];
varying vec4 point_c[4];

out vec3 frag_color;

void main(){
    vec4 mid_point = (geom_coord[0] + geom_coord[1])/2;
    vec2 dir_vec = normalize((geom_coord[1] - geom_coord[0]).xy);
    vec3 orto_vec = normalize(cross(vec3(dir_vec, 0), vec3(0, 0, 1)));
    point_a[0] = vec4(geom_coord[0].xyz + orto_vec * antialias_length, 1.0);
    point_a[1] = vec4(geom_coord[0].xyz + orto_vec * antialias_length/2, 1.0);
    point_a[2] = vec4(geom_coord[0].xyz - orto_vec * antialias_length/2, 1.0);
    point_a[3] = vec4(geom_coord[0].xyz - orto_vec * antialias_length, 1.0);
    point_b[0] = vec4(mid_point.xyz + orto_vec * antialias_length, 1.0);
    point_b[1] = vec4(mid_point.xyz + orto_vec * antialias_length/2, 1.0);
    point_b[2] = vec4(mid_point.xyz - orto_vec * antialias_length/2, 1.0);
    point_b[3] = vec4(mid_point.xyz - orto_vec * antialias_length, 1.0);
    point_c[0] = vec4(geom_coord[1].xyz + orto_vec * antialias_length, 1.0);
    point_c[1] = vec4(geom_coord[1].xyz + orto_vec * antialias_length/2, 1.0);
    point_c[2] = vec4(geom_coord[1].xyz - orto_vec * antialias_length/2, 1.0);
    point_c[3] = vec4(geom_coord[1].xyz - orto_vec * antialias_length, 1.0);
    
    gl_Position = proj_mat * point_a[0];
    frag_color = alias_color;
    EmitVertex();
    gl_Position = proj_mat * point_b[0];
    frag_color = alias_color;
    EmitVertex();
    gl_Position = proj_mat * point_a[1];
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * point_b[1];
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0];
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * mid_point;
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * point_a[2];
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * point_b[2];
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * point_a[3];
    frag_color = alias_color;
    EmitVertex();
    gl_Position = proj_mat * point_b[3];
    frag_color = alias_color;
    EmitVertex();
    EndPrimitive();
    
    gl_Position = proj_mat * point_b[0];
    frag_color = alias_color;
    EmitVertex();
    gl_Position = proj_mat * point_c[0];
    frag_color = alias_color;
    EmitVertex();
    gl_Position = proj_mat * point_b[1];
    frag_color = geom_color[1];
    EmitVertex();
    gl_Position = proj_mat * point_c[1];
    frag_color = geom_color[1];
    EmitVertex();
    gl_Position = proj_mat * mid_point;
    frag_color = geom_color[1];
    EmitVertex();
    gl_Position = proj_mat * geom_coord[1];
    frag_color = geom_color[1];
    EmitVertex();
    gl_Position = proj_mat * point_b[2];
    frag_color = geom_color[1];
    EmitVertex();
    gl_Position = proj_mat * point_c[2];
    frag_color = geom_color[1];
    EmitVertex();
    gl_Position = proj_mat * point_b[3];
    frag_color = alias_color;
    EmitVertex();
    gl_Position = proj_mat * point_c[3];
    frag_color = alias_color;
    EmitVertex();
    EndPrimitive();
}
"""
f_shader_antialias = """
#version 330

in vec3 frag_color;

out vec4 final_color;

void main(){
    final_color = vec4(frag_color, 1);
}
"""

v_shader_pseudospheres = """
#version 330

uniform mat4 model_mat;
uniform mat4 view_mat;

in vec3 vert_coord;
in vec3 vert_color;
in float vert_rad;

out vec4 geom_coord;
out vec3 geom_color;
out float geom_rad;

void main(){
    geom_color = vert_color;
    geom_coord = view_mat * model_mat * vec4(vert_coord, 1);
    geom_rad = vert_rad;
}
"""
g_shader_pseudospheres = """
#version 330

layout (points) in;
layout (triangle_strip, max_vertices = 13) out;

uniform mat4 proj_mat;

const float cos45 = 0.7071067811865476;
const float sin45 = 0.7071067811865476;
const vec3 shadow_col = vec3(0, 0, 0);

in vec4 geom_coord[];
in vec3 geom_color[];
in float geom_rad[];

out vec3 frag_color;

void main(){
    gl_Position = proj_mat * (geom_coord[0] + vec4(geom_rad[0], 0, 0, 0)); // Point 1
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 2
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos45*geom_rad[0], sin45*geom_rad[0], 0, 0)); // Point 3
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(0, geom_rad[0], 0, 0)); // Point 4
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 5
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos45*geom_rad[0], sin45*geom_rad[0], 0, 0)); // Point 6
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-geom_rad[0], 0, 0, 0)); // Point 7
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 8
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos45*geom_rad[0], -sin45*geom_rad[0], 0, 0)); // Point 9
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(0, -geom_rad[0], 0, 0)); // Point 10
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 11
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos45*geom_rad[0], -sin45*geom_rad[0], 0, 0)); // Point 12
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(geom_rad[0], 0, 0, 0)); // Point 13
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    EndPrimitive();
}
"""
g_shader_pseudospheres2 = """
#version 330

layout (points) in;
layout (triangle_strip, max_vertices = 19) out;

uniform mat4 proj_mat;

const float cos30 = 0.866025404;
const float sin30 = 0.5;
const float cos60 = 0.5;
const float sin60 = 0.866025404;
const vec3 shadow_col = vec3(0, 0, 0);

in vec4 geom_coord[];
in vec3 geom_color[];
in float geom_rad[];

out vec3 frag_color;

void main(){
    gl_Position = proj_mat * (geom_coord[0] + vec4(geom_rad[0], 0, 0, 0)); // Point 1
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 2
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos30*geom_rad[0], sin30*geom_rad[0], 0, 0)); // Point 3
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos60*geom_rad[0], sin60*geom_rad[0], 0, 0)); // Point 4
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 5
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(0, geom_rad[0], 0, 0)); // Point 6
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos60*geom_rad[0], sin60*geom_rad[0], 0, 0)); // Point 7
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 8
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos30*geom_rad[0], sin30*geom_rad[0], 0, 0)); // Point 9
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-geom_rad[0], 0, 0, 0)); // Point 10
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 11
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos30*geom_rad[0], -sin30*geom_rad[0], 0, 0)); // Point 12
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos60*geom_rad[0], -sin60*geom_rad[0], 0, 0)); // Point 13
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 14
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(0, -geom_rad[0], 0, 0)); // Point 15
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos60*geom_rad[0], -sin60*geom_rad[0], 0, 0)); // Point 16
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 17
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos30*geom_rad[0], -sin30*geom_rad[0], 0, 0)); // Point 18
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(geom_rad[0], 0, 0, 0)); // Point 19
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    EndPrimitive();
}
"""
g_shader_pseudospheres3 = """
#version 330

layout (points) in;
layout (triangle_strip, max_vertices = 25) out;

uniform mat4 proj_mat;

const float cos22 = 0.9238795325112867;
const float cos45 = 0.7071067811865476;
const float cos67 = 0.3826834323650898;
const float sin22 = 0.3826834323650898;
const float sin45 = 0.7071067811865475;
const float sin67 = 0.9238795325112867;
const vec3 shadow_col = vec3(0, 0, 0);

in vec4 geom_coord[];
in vec3 geom_color[];
in float geom_rad[];

out vec3 frag_color;

void main(){
    gl_Position = proj_mat * (geom_coord[0] + vec4(geom_rad[0], 0, 0, 0)); // Point 1
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 2
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos22*geom_rad[0], sin22*geom_rad[0], 0, 0)); // Point 3
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos45*geom_rad[0], sin45*geom_rad[0], 0, 0)); // Point 4
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 5
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos67*geom_rad[0], sin67*geom_rad[0], 0, 0)); // Point 6
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(0, geom_rad[0], 0, 0)); // Point 7
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 8
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos67*geom_rad[0], sin67*geom_rad[0], 0, 0)); // Point 9
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos45*geom_rad[0], sin45*geom_rad[0], 0, 0)); // Point 10
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 11
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos22*geom_rad[0], sin22*geom_rad[0], 0, 0)); // Point 12
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-geom_rad[0], 0, 0, 0)); // Point 13
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 14
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos22*geom_rad[0], -sin22*geom_rad[0], 0, 0)); // Point 15
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos45*geom_rad[0], -sin45*geom_rad[0], 0, 0)); // Point 16
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 17
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos67*geom_rad[0], -sin67*geom_rad[0], 0, 0)); // Point 18
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(0, -geom_rad[0], 0, 0)); // Point 19
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 20
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos67*geom_rad[0], -sin67*geom_rad[0], 0, 0)); // Point 21
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos45*geom_rad[0], -sin45*geom_rad[0], 0, 0)); // Point 22
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 23
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos22*geom_rad[0], -sin22*geom_rad[0], 0, 0)); // Point 24
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(geom_rad[0], 0, 0, 0)); // Point 25
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    EndPrimitive();
}
"""
g_shader_pseudospheres4 = """
#version 330

layout (points) in;
layout (triangle_strip, max_vertices = 31) out;

uniform mat4 proj_mat;

const float cos18 = 0.9510565162951535;
const float cos36 = 0.8090169943749475;
const float cos54 = 0.5877852522924731;
const float cos72 = 0.3090169943749474;
const float sin18 = 0.3090169943749474;
const float sin36 = 0.5877852522924731;
const float sin54 = 0.8090169943749475;
const float sin72 = 0.9510565162951535;
const vec3 shadow_col = vec3(0, 0, 0);

in vec4 geom_coord[];
in vec3 geom_color[];
in float geom_rad[];

out vec3 frag_color;

void main(){
    gl_Position = proj_mat * (geom_coord[0] + vec4(geom_rad[0], 0, 0, 0)); // Point 1
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 2
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos18*geom_rad[0], sin18*geom_rad[0], 0, 0)); // Point 3
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos36*geom_rad[0], sin36*geom_rad[0], 0, 0)); // Point 4
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 5
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos54*geom_rad[0], sin54*geom_rad[0], 0, 0)); // Point 6
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos72*geom_rad[0], sin72*geom_rad[0], 0, 0)); // Point 7
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 8
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(0, geom_rad[0], 0, 0)); // Point 9
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos72*geom_rad[0], sin72*geom_rad[0], 0, 0)); // Point 10
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 11
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos54*geom_rad[0], sin54*geom_rad[0], 0, 0)); // Point 12
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos36*geom_rad[0], sin36*geom_rad[0], 0, 0)); // Point 13
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 14
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos18*geom_rad[0], sin18*geom_rad[0], 0, 0)); // Point 15
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-geom_rad[0], 0, 0, 0)); // Point 16
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 17
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos18*geom_rad[0], -sin18*geom_rad[0], 0, 0)); // Point 18
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos36*geom_rad[0], -sin36*geom_rad[0], 0, 0)); // Point 19
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 20
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos54*geom_rad[0], -sin54*geom_rad[0], 0, 0)); // Point 21
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos72*geom_rad[0], -sin72*geom_rad[0], 0, 0)); // Point 22
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 23
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(0, -geom_rad[0], 0, 0)); // Point 24
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos72*geom_rad[0], -sin72*geom_rad[0], 0, 0)); // Point 25
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 26
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos54*geom_rad[0], -sin54*geom_rad[0], 0, 0)); // Point 27
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos36*geom_rad[0], -sin36*geom_rad[0], 0, 0)); // Point 28
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 29
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos18*geom_rad[0], -sin18*geom_rad[0], 0, 0)); // Point 30
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(geom_rad[0], 0, 0, 0)); // Point 31
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    EndPrimitive();
}
"""
g_shader_pseudospheres5 = """
#version 330

layout (points) in;
layout (triangle_strip, max_vertices = 37) out;

uniform mat4 proj_mat;

const float cos15 = 0.9659258262890683;
const float cos30 = 0.8660254037844387;
const float cos45 = 0.7071067811865476;
const float cos60 = 0.5000000000000001;
const float cos75 = 0.2588190451025207;
const float sin15 = 0.2588190451025207;
const float sin30 = 0.4999999999999999;
const float sin45 = 0.7071067811865475;
const float sin60 = 0.8660254037844386;
const float sin75 = 0.9659258262890683;
const vec3 shadow_col = vec3(0, 0, 0);

in vec4 geom_coord[];
in vec3 geom_color[];
in float geom_rad[];

out vec3 frag_color;

void main(){
    gl_Position = proj_mat * (geom_coord[0] + vec4(geom_rad[0], 0, 0, 0)); // Point 1
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 2
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos15*geom_rad[0], sin15*geom_rad[0], 0, 0)); // Point 3
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos30*geom_rad[0], sin30*geom_rad[0], 0, 0)); // Point 4
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 5
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos45*geom_rad[0], sin45*geom_rad[0], 0, 0)); // Point 6
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos60*geom_rad[0], sin60*geom_rad[0], 0, 0)); // Point 7
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 8
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos75*geom_rad[0], sin75*geom_rad[0], 0, 0)); // Point 9
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(0, geom_rad[0], 0, 0)); // Point 10
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 11
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos75*geom_rad[0], sin75*geom_rad[0], 0, 0)); // Point 12
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos60*geom_rad[0], sin60*geom_rad[0], 0, 0)); // Point 13
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 14
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos45*geom_rad[0], sin45*geom_rad[0], 0, 0)); // Point 15
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos30*geom_rad[0], sin30*geom_rad[0], 0, 0)); // Point 16
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 17
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos15*geom_rad[0], sin15*geom_rad[0], 0, 0)); // Point 18
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-geom_rad[0], 0, 0, 0)); // Point 19
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 20
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos15*geom_rad[0], -sin15*geom_rad[0], 0, 0)); // Point 21
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos30*geom_rad[0], -sin30*geom_rad[0], 0, 0)); // Point 22
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 23
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos45*geom_rad[0], -sin45*geom_rad[0], 0, 0)); // Point 24
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos60*geom_rad[0], -sin60*geom_rad[0], 0, 0)); // Point 25
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 26
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(-cos75*geom_rad[0], -sin75*geom_rad[0], 0, 0)); // Point 27
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(0, -geom_rad[0], 0, 0)); // Point 28
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 29
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos75*geom_rad[0], -sin75*geom_rad[0], 0, 0)); // Point 30
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos60*geom_rad[0], -sin60*geom_rad[0], 0, 0)); // Point 31
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 32
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos45*geom_rad[0], -sin45*geom_rad[0], 0, 0)); // Point 33
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos30*geom_rad[0], -sin30*geom_rad[0], 0, 0)); // Point 34
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * geom_coord[0]; // Point 35
    frag_color = geom_color[0];
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(cos15*geom_rad[0], -sin15*geom_rad[0], 0, 0)); // Point 36
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    gl_Position = proj_mat * (geom_coord[0] + vec4(geom_rad[0], 0, 0, 0)); // Point 37
    frag_color = mix(geom_color[0], shadow_col, 0.5);
    EmitVertex();
    EndPrimitive();
}
"""
f_shader_pseudospheres = """
#version 330

in vec3 frag_color;

out vec4 final_color;

void main(){
    final_color = vec4(frag_color, 1);
    //final_color = mix(vec4(frag_color, 1), vec4(0, 0, 0, 1), 0.2);
}
"""

v_shader_geom_cones = """
#version 330

uniform mat4 model_mat;
uniform mat4 view_mat;
uniform mat4 proj_mat;

in vec3 vert_coord;
in vec3 vert_color;
in vec3 vert_norm;

out vec3 frag_coord;
out vec3 frag_color;
out vec3 frag_norm;

void main(){
    frag_coord = (view_mat * model_mat * vec4(vert_coord, 1.0)).xyz;
    frag_color = vert_color;
    frag_norm = mat3(transpose(inverse(model_mat))) * vert_norm;
    gl_Position = proj_mat * vec4(frag_coord, 1.0);
}
"""
f_shader_geom_cones = """
#version 330

struct Light {
   vec3 position;
   //vec3 color;
   vec3 intensity;
   //vec3 specular_color;
   float ambient_coef;
   float shininess;
};

uniform Light my_light;

in vec3 frag_coord;
in vec3 frag_color;
in vec3 frag_norm;

out vec4 final_color;

void main(){
    vec3 normal = normalize(frag_norm);
    vec3 vert_to_light = normalize(my_light.position);
    vec3 vert_to_cam = normalize(frag_coord);
    
    // Ambient Component
    vec3 ambient = my_light.ambient_coef * frag_color * my_light.intensity;
    
    // Diffuse component
    float diffuse_coef = max(0.0, dot(normal, vert_to_light));
    vec3 diffuse = diffuse_coef * frag_color * my_light.intensity;
    
    // Specular component
    float specular_coef = 0.0;
    if (diffuse_coef > 0.0)
        specular_coef = pow(max(0.0, dot(vert_to_cam, reflect(-vert_to_light, normal))), my_light.shininess);
    vec3 specular = specular_coef * my_light.intensity;
    specular = specular * (vec3(1) - diffuse);
    final_color = vec4(ambient + diffuse + specular, 1.0);
}
"""

v_shader_arrow = """
#version 330

uniform mat4 model_mat;
uniform mat4 view_mat;

in vec3 vert_coord;
in vec3 vert_color;

out vec3 geom_coord;
out vec3 geom_color;

void main(){
    geom_coord = (view_mat * model_mat * vec4(vert_coord, 1.0)).xyz;
    geom_color = vert_color;
}
"""
g_shader_arrow = """
#version 330

layout (triangles) in;
layout (triangle_strip, max_vertices = 3) out;

uniform mat4 proj_mat;

in vec3 geom_coord[];
in vec3 geom_color[];

varying vec3 vec_a;
varying vec3 vec_b;

out vec3 frag_coord;
out vec3 frag_color;
out vec3 frag_norm;

void main(){
    vec_a = normalize(geom_coord[2] - geom_coord[0]);
    vec_b = normalize(geom_coord[2] - geom_coord[1]);
    gl_Position = proj_mat * vec4(geom_coord[0], 1.0);
    frag_coord = geom_coord[0];
    frag_color = geom_color[0];
    frag_norm = cross(vec_b, vec_a);
    EmitVertex();
    gl_Position = proj_mat * vec4(geom_coord[1], 1.0);
    frag_coord = geom_coord[1];
    frag_color = geom_color[1];
    frag_norm = cross(vec_b, vec_a);
    EmitVertex();
    gl_Position = proj_mat * vec4(geom_coord[2], 1.0);
    frag_coord = geom_coord[2];
    frag_color = geom_color[2];
    frag_norm = cross(vec_b, vec_a);
    EmitVertex();
    EndPrimitive();
}
"""
f_shader_arrow = """
#version 330

struct Light {
    vec3 position;
    //vec3 color;
    vec3 intensity;
    //vec3 specular_color;
    float ambient_coef;
    float shininess;
};

uniform Light my_light;

in vec3 frag_coord;
in vec3 frag_color;
in vec3 frag_norm;

out vec4 final_color;

void main(){
    vec3 normal = normalize(frag_norm);
    vec3 vert_to_light = normalize(my_light.position);
    vec3 vert_to_cam = normalize(frag_coord);
    
    // Ambient Component
    vec3 ambient = my_light.ambient_coef * frag_color * my_light.intensity;
    
    // Diffuse component
    float diffuse_coef = max(0.0, dot(normal, vert_to_light));
    vec3 diffuse = diffuse_coef * frag_color * my_light.intensity;
    
    // Specular component
    float specular_coef = 0.0;
    if (diffuse_coef > 0.0)
        specular_coef = pow(max(0.0, dot(vert_to_cam, reflect(vert_to_light, normal))), my_light.shininess);
    vec3 specular = specular_coef * my_light.intensity;
    specular = specular * (vec3(1) - diffuse);
    final_color = vec4(ambient + diffuse + specular, 1.0);
}
"""

v_shader_select_box = """
#version 330

//uniform mat4 model_mat;
//uniform mat4 view_mat;
//uniform mat4 proj_mat;

in vec3 vert_coord;
in vec3 vert_color;

out vec3 frag_color;

void main(){
    gl_Position = vec4(vert_coord, 1.0);
    //gl_Position = view_mat * vec4(vert_coord, 1.0);
    //gl_Position = proj_mat * view_mat * model_mat * vec4(vert_coord, 1.0);
    frag_color = vert_color;
}
"""
f_shader_select_box = """
#version 330

in vec3 frag_color;

out vec4 final_color;

void main(){
    final_color = vec4(frag_color, 1.0);
}
"""

v_shader_add_points = """
#version 330

uniform mat4 model_mat;
uniform mat4 view_mat;
uniform mat4 proj_mat;

in vec3 vert_coord;
in vec3 vert_color;

out vec3 frag_color;

void main(){
    //gl_Position = vec4(vert_coord, 1.0);
    gl_Position = proj_mat * view_mat * model_mat * vec4(vert_coord, 1.0);
    frag_color = vert_color;
}
"""
f_shader_add_points = """
#version 330

in vec3 frag_color;

out vec4 final_color;

void main(){
    final_color = vec4(frag_color, 1.0);
}
"""

v_shader_edit_mode = """
#version 330

uniform mat4 model_mat;
uniform mat4 view_mat;
uniform mat4 proj_mat;

in vec3 vert_coord;
in vec3 vert_centr;
in vec3 vert_color;

varying vec3 vert_norm;

out vec3 frag_coord;
out vec3 frag_color;
out vec3 frag_norm;

void main(){
    mat4 modelview = view_mat * model_mat;
    gl_Position = proj_mat * modelview * vec4(vert_coord, 1.0);
    vert_norm = normalize(vert_coord - vert_centr);
    frag_coord = -vec3(modelview * vec4(vert_coord, 1.0));
    frag_norm = mat3(transpose(inverse(model_mat))) * vert_norm;
    frag_color = vert_color;
}
"""
f_shader_edit_mode = """
#version 330

struct Light {
    vec3 position;
    //vec3 color;
    vec3 intensity;
    //vec3 specular_color;
    float ambient_coef;
    float shininess;
};

uniform Light my_light;

in vec3 frag_coord;
in vec3 frag_color;
in vec3 frag_norm;

out vec4 final_color;

void main(){
    vec3 normal = normalize(frag_norm);
    vec3 vert_to_light = normalize(my_light.position);
    vec3 vert_to_cam = normalize(frag_coord);
    
    // Ambient Component
    vec3 ambient = my_light.ambient_coef * frag_color * my_light.intensity;
    
    // Diffuse component
    float diffuse_coef = max(0.0, dot(normal, vert_to_light));
    vec3 diffuse = diffuse_coef * frag_color * my_light.intensity;
    
    // Specular component
    float specular_coef = 0.0;
    if (diffuse_coef > 0.0)
        specular_coef = pow(max(0.0, dot(vert_to_cam, reflect(-vert_to_light, normal))), my_light.shininess);
    vec3 specular = specular_coef * my_light.intensity;
    specular = specular * (vec3(1) - diffuse);
    
    final_color = vec4(ambient + diffuse + specular, 1.0);
}
"""

v_shader_texture =  """
#version 330

uniform mat4 model_mat;
uniform mat4 view_mat;
uniform mat4 proj_mat;

in vec3 vert_coord;
in vec2 vert_text;

out vec2 frag_text;

void main(){
    gl_Position = proj_mat * view_mat * model_mat * vec4(vert_coord, 1.0);
    frag_text = vert_text;
}
"""
f_shader_texture = """
#version 330

uniform sampler2D textu;

in vec2 frag_text;

out vec4 final_color;

void main(){
    final_color = texture(textu, frag_text);
}
"""
