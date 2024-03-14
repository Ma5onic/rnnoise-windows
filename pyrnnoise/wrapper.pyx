# rnnoise_wrapper.pyx
# cython: language_level=3

cdef extern from "rnnoise.h":
    ctypedef struct DenoiseState:
        pass

    DenoiseState* rnnoise_create(void* model)
    int rnnoise_destroy(DenoiseState* st)
    float rnnoise_process_frame(DenoiseState* st, float* out, float* inp)  # Avoid using 'in' as an argument name

cimport cython
from cpython.pycapsule cimport PyCapsule_New, PyCapsule_GetPointer

@cython.boundscheck(False)
@cython.wraparound(False)
def create_rnnoise():
    return PyCapsule_New(rnnoise_create(NULL), "DenoiseState", NULL)

@cython.boundscheck(False)
@cython.wraparound(False)
def destroy_rnnoise(capsule):
    cdef DenoiseState* st = <DenoiseState*>PyCapsule_GetPointer(capsule, "DenoiseState")
    rnnoise_destroy(st)

@cython.boundscheck(False)
@cython.wraparound(False)
def process_frame(capsule, float[:] frame_in):
    cdef float[:] frame_out = frame_in.copy()  # Assuming in-place modification is desired
    cdef DenoiseState* st = <DenoiseState*>PyCapsule_GetPointer(capsule, "DenoiseState")
    rnnoise_process_frame(st, &frame_out[0], &frame_in[0])
    return frame_out