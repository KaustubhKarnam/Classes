import pytest
import numpy as np
from geometry_lib import *

def test__sub_point_point__returns_vector():
    p1 = Point((0,1,0))
    p2 = Point((1,2,3))
    v1 = Vector([1, 1, 3])
    v2 = p2-p1
    if v1 == v2:
        return True

def test__sum_point_vector__returns_point():
    p1 = Point((0,1,0))
    p2 = Vector((1,2,3))
    v1 = Point([1, 3, 3])
    v2 = p1+p2
    if v1 == v2:
        return True

def test__sum_vector_point__returns_point():
    p1 = Point((0,1,0))
    p2 = Vector((1,2,3))
    v1 = Point([1, 3, 3])
    v2 = p2+p1
    if v1 == v2:
        return True 

def test__sum_point_point__returns_error():
    p1 = Point((0,1,0))
    p2 = Point((1,2,3))
    v2 = p2+p1

def test__sum_vector_vector__returns_vector():
    p1 = Vector((0,1,0))
    p2 = Vector((1,2,3))
    v1 = Vector([1, 3, 3])
    v2 = p2+p1
    if v1 == v2:
        return True    

def test__sub_vector_vector__returns_vector():
    p1 = Vector((0,1,0))
    p2 = Vector((1,2,3))
    v1 = Vector([1, 1, 3])
    v2 = p2-p1
    if v1 == v2:
        return True 