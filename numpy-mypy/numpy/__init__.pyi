"""
Numpy's mypy stub. Only type declarations for ndarray, the scalar hierarchy and array creation
methods are provided.
"""

from typing import (Any, Callable, Dict, Generic, Iterator, List, Optional, Sequence, Tuple, Type,
                    TypeVar, Union)

class dtype: ...
_dtype = dtype


class flagsobj:
    """numpy.flagsobj"""
    aligned = None       # type: bool
    behaved = None       # type: bool
    c_contiguous = None  # type: bool
    carray = None        # type: bool
    contiguous = None    # type: bool
    f_contiguous = None  # type: bool
    farray = None        # type: bool
    fnc = None           # type: bool
    forc = None          # type: bool
    fortran = None       # type: bool
    owndata = None       # type: bool
    updateifcopy = None  # type: bool
    writeable = None     # type: bool
    def __getitem__(self, item: str) -> bool: ...

#
# Type variables. _T wasn't used to avoid confusions with ndarray's "T" attribute.
#

_S = TypeVar('_S')
_U = TypeVar('_U')

#
# Auxiliary types
#

ShapeType = Union[int, Tuple[int, ...]]
AxesType = Union[int, Tuple[int, ...]]
OrderType = Union[str, Sequence[str]]
DtypeType = Union[dtype, type]
NdarrayLikeType = TypeVar('NdarrayLikeType', bound='ndarray')

class _ArrayLike(Generic[_S]):
    """
    "array-like" interface that both numpy.ndarray and all scalars (descendants of numpy.generic)
    implement this interface.
    """
    #
    # Array-like structures attributes
    #
    T = None         # type: _ArrayLike[_S]
    data = None      # type: Any
    dtype = None     # type: _dtype
    flags = None     # type: flagsobj
    flat = None      # type: Iterator[_ArrayLike[_S]]
    imag = None      # type: _ArrayLike[_S]
    real = None      # type: _ArrayLike[_S]
    size = None      # type: int
    itemsize = None  # type: int
    nbytes = None    # type: int
    ndim = None      # type: int
    shape = None     # type: ShapeType
    strides = None   # type: Tuple[int]
    base = None      # type: Optional[_ArrayLike[_S]]

    #
    # Array-like methods
    #

    # Once this issue https://github.com/python/mypy/issues/1907 is resolved, most methods that
    # have an 'out' argument, will be implemented using overload instead of with a Union
    # result. mypy is smart enough to assign the proper type (_ArrayLike[_U]) when out is present
    # but it falls back to the union when it's not.
    def all(self, axis: Optional[AxesType]=None, out: Optional['_ArrayLike[_U]']=None,
            keepdims: Optional[bool]=None) -> Union['_ArrayLike[_U]', '_ArrayLike[bool]']: ...

    def any(self, axis: Optional[AxesType]=None, out: Optional['_ArrayLike[_U]']=None,
            keepdims: Optional[bool]=None) -> Union['_ArrayLike[_U]', '_ArrayLike[bool]']: ...

    def argmax(self, axis: Optional[int]=None,
               out: Optional['_ArrayLike[_U]']=None) -> Union['_ArrayLike[_U]', '_ArrayLike[int]']: ...

    def argmin(self, axis: Optional[int]=None,
               out: Optional['_ArrayLike[_U]']=None) -> Union['_ArrayLike[_U]', '_ArrayLike[int]']: ...

    def argpartition(self, kth: Union[int, Sequence[int]], axis: Optional[int]=-1,
                     kind: Optional[str]='introselect',
                     order: Optional[OrderType]=None) -> '_ArrayLike[int]': ...

    def argsort(self, axis: Optional[int]=None, kind: Optional[str]='quicksort',
                order: Optional[OrderType]=None) -> '_ArrayLike[int]': ...

    def astype(self, dtype: Any, order: Optional[str]='K',
               casting: Optional[str]='unsafe', subok: Optional[bool]=None,
               copy: Optional[bool]=None) -> '_ArrayLike[Any]': ...

    def byteswap(self, inplace: Optional[bool]=False) -> '_ArrayLike[_S]': ...

    def choose(self, choices:Sequence['_ArrayLike[Any]'], out: Optional['_ArrayLike[Any]']=None,
               mode: Optional['str']='raise') -> '_ArrayLike[Any]': ...

    def clip(self, a_min: Any, a_max: Any,
             out: Optional['_ArrayLike[_U]']=None) -> Union['_ArrayLike[_S]', '_ArrayLike[_U]']: ...

    def compress(self, condition: Sequence[bool], axis: Optional[int]=None,
                 out: Optional['_ArrayLike[_U]']=None) -> Union['_ArrayLike[_S]', '_ArrayLike[_U]']: ...

    def conj(self) -> '_ArrayLike[_S]': ...

    def conjugate(self) -> '_ArrayLike[_S]': ...

    def copy(self, order: Optional['str']='C') -> '_ArrayLike[_S]': ...

    def cumprod(self, axis: Optional[int]=None, dtype: Optional[Any]=None,
                out: Optional['_ArrayLike[Any]']=None) -> '_ArrayLike[Any]': ...

    def cumsum(self, axis: Optional[int]=None, dtype: Optional[DtypeType]=None,
                out: Optional['_ArrayLike[Any]']=None) -> '_ArrayLike[Any]': ...

    def diagonal(self, offset: Optional[int]=0, axis1: Optional[int]=0,
                 axis2: Optional[int]=1) -> '_ArrayLike[_S]': ...

    def dot(self, b: '_ArrayLike[Any]',
            out: Optional['_ArrayLike[Any]']=None) -> '_ArrayLike[Any]': ...

    def dump(self, file: 'str') -> None: ...

    def dumps(self) -> 'str': ...

    def fill(self, value: Any) -> None: ...

    def flatten(self, order: Optional[str]='C') -> '_ArrayLike[_S]': ...

    def getfield(self, dtype: DtypeType, offset: Optional[int]=0) -> '_ArrayLike[Any]': ...

    def item(self, args: Optional[AxesType]) -> generic: ...

    def itemset(self, arg0: Union[int, Tuple[int, ...]], arg1: Optional[Any]=None) -> None: ...

    def max(self, axis: Optional[AxesType]=None,
            out: Optional['_ArrayLike[_U]']=None) -> Union['_ArrayLike[_S]', '_ArrayLike[_U]']: ...

    def mean(self, axis: Optional[AxesType]=None, dtype: Optional[Any]=None,
             out=Optional['_ArrayLike[_U]'], keepdims: Optional[bool]=False) -> '_ArrayLike[Any]': ...

    def min(self, axis: Optional[AxesType]=None,
            out: Optional['_ArrayLike[_U]']=None) -> Union['_ArrayLike[_S]', '_ArrayLike[_U]']: ...

    def newbyteorder(self, new_order: Optional['str']='S') -> '_ArrayLike[Any]': ...

    def nonzero(self) -> '_ArrayLike[int]': ...

    def partition(self, kth: AxesType, axis: Optional[int]=-1, kind: Optional[str]='introselect',
                  order: Optional[OrderType]=None) -> None: ...

    def prod(self, axis: Optional[AxesType]=None, dtype: Optional[DtypeType]=None,
             out: Optional['_ArrayLike[_U]']=None, keepdims: Optional[bool]=False) -> '_ArrayLike[Any]': ...

    def ptp(self, axis: Optional[int]=None,
            out: Optional['_ArrayLike[_U]']=None) -> Union['_ArrayLike[_S]', '_ArrayLike[_U]']: ...

    def put(self, ind: Sequence[Any], v: Sequence[Any], mode: Optional[str]='raise') -> None: ...

    def ravel(self, order: Optional[str]='C') -> '_ArrayLike[_S]': ...

    def repeat(self, repeats: Union[int, Sequence[int]],
               axis: Optional[int]=None) -> '_ArrayLike[_S]': ...

    def reshape(self, newshape: ShapeType,
                order: Optional[str]='C') -> '_ArrayLike[_S]': ...

    def resize(self, new_shape: ShapeType, refcheck: Optional[bool]=True) -> None: ...

    def round(self, decimals: int=0,
              out: Optional['_ArrayLike[_U]']=None) -> Union['_ArrayLike[_S]', '_ArrayLike[_U]']: ...

    def searchsorted(self, v: Union[Any, Sequence[Any]], side: Optional[str]='left',
                     sorter: Optional[Any]=None) -> '_ArrayLike[int]': ...

    def setfield(self, val: Any, dtype: DtypeType, offset: Optional[int]=0) -> None: ...

    def setflags(self, write: Optional[bool]=None, align: Optional[bool]=None,
                 uic: Optional[bool]=None) -> None: ...

    def sort(self, axis: Optional[int]=-1, kind: Optional[str]='quicksort',
             order: Optional[OrderType]=None) -> None: ...

    def squeeze(self, axis: Optional[AxesType]) -> '_ArrayLike[_S]': ...

    def std(self, axis: Optional[AxesType]=None, dtype: Optional[DtypeType]=None,
            out=Optional['_ArrayLike[_U]'], ddof: Optional[int]=0,
            keepdims: Optional[bool]=False) -> '_ArrayLike[Any]': ...

    def sum(self, axis: Optional[AxesType]=None, dtype=Optional[DtypeType],
            out: Optional['_ArrayLike[_U]']=None,
            keepdims: Optional[bool]=False) -> '_ArrayLike[Any]': ...

    def swapaxes(self, axis1: int, axis2: int) -> '_ArrayLike[_S]': ...

    def take(self, indices: Sequence[int], axis: Optional[int]=None,
             out: Optional['_ArrayLike[_U]']=None,
             mode: Optional[str]='raise') -> Union['_ArrayLike[_S]', '_ArrayLike[_U]']: ...

    def tobytes(self, order: Optional[str]='C') -> bytes: ...

    def tofile(self, fid: Any, sep: Optional[str]='',  # TODO fix fid definition (There's a bug in mypy io's namespace https://github.com/python/mypy/issues/1462)
               format: Optional[str]='%s') -> None: ...

    def tolist(self) -> List[Any]: ...

    def tostring(self, order: Optional[str]='C') -> bytes: ...

    def trace(self, offset: Optional[int]=0, axis1: Optional[int]=0, axis2: Optional[int]=1,
              dtype=Optional[DtypeType], out=Optional['_ArrayLike[_U]']) -> '_ArrayLike[Any]': ...

    def transpose(self, axes: Optional[AxesType]) -> '_ArrayLike[_S]': ...

    def var(self, axis: Optional[AxesType]=None, dtype=Optional[DtypeType],
            out=Optional['_ArrayLike[_U]'], ddof: Optional[int]=0, keepdims: Optional[bool]=False) -> '_ArrayLike[Any]': ...

    def view(self, dtype: Optional[Union[DtypeType, Type[NdarrayLikeType]]]=None,
             type: Optional[type]=None) -> '_ArrayLike[Any]': ...

    #
    # Magic methods
    #

    def __abs__(self) -> '_ArrayLike[_S]': ...

    def __add__(self, value: Any) -> '_ArrayLike[Any]': ...

    def __and__(self, value: Any) -> bool: ...

    def __array__(self, dtype: Optional[DtypeType]=None) -> '_ArrayLike[Any]': ...

    def __array_prepare__(self, context: Optional[Any]=None) -> '_ArrayLike[Any]': ...

    def __array_wrap__(self, context: Optional[Any]=None) -> '_ArrayLike[Any]': ...

    def __bool__(self) -> bool: ...

    def __complex__(self) -> complex: ...

    def __contains__(self, key: Any) -> bool: ...

    def __copy__(self) -> '_ArrayLike[_S]': ...

    def __deepcopy__(self) -> '_ArrayLike[_S]': ...

    def __delattr__(self, name: str) -> None: ...

    def __delitem__(self, key: str) -> None: ...

    def __dir__(self) -> List[str]: ...

    def __divmod__(self, value: Any) -> Tuple['_ArrayLike[int]', '_ArrayLike[float]']: ...

    def __eq__(self, value: Any) -> '_ArrayLike[bool]': ...  # type: ignore

    def __float__(self) -> float: ...

    def __floordiv__(self, value: Any) -> '_ArrayLike[int]': ...

    def __ge__(self, value: Any) -> '_ArrayLike[bool]': ...

    def __getattribute__(self, name: str) -> Any: ...

    def __getitem__(self, key: str) -> '_ArrayLike[_S]': ...

    def __gt__(self, value: Any) -> '_ArrayLike[bool]': ...

    def __iadd__(self, value: Any) -> None: ...

    def __iand__(self, value: Any) -> None: ...

    def __ifloordiv__(self, value: Any) -> None: ...

    def __ilshift__(self, value: Any) -> None: ...

    def __imatmul__(self, value: '_ArrayLike[Any]') -> None: ...

    def __imod__(self, value: Any) -> None: ...

    def __imul__(self, value: Any) -> None: ...

    def __index__(self) -> int: ...

    def __int__(self) -> int: ...

    def __invert__(self) -> '_ArrayLike[_S]': ...

    def __ior__(self, value: Any) -> None: ...

    def __ipow__(self, value: Any) -> None: ...

    def __irshift__(self, value: Any) -> None: ...

    def __isub__(self, value: Any) -> None: ...

    def __iter__(self) -> Iterator['_ArrayLike[_S]']: ...

    def __itruediv__(sel, value: Any) -> None: ...

    def __ixor__(self, value: Any) -> None: ...

    def __le__(self, value: Any) -> '_ArrayLike[bool]': ...

    def __len__(self) -> int: ...

    def __lshift__(self, value: Any) -> '_ArrayLike[_S]': ...

    def __lt__(self, value: Any) -> '_ArrayLike[bool]': ...

    def __matmul__(self, value: '_ArrayLike[Any]') -> '_ArrayLike[Any]': ...

    def __mod__(self, value: Any) -> '_ArrayLike[_S]': ...

    def __mul__(self, value: Any) -> '_ArrayLike[Any]': ...

    def __ne__(self, value: Any) -> '_ArrayLike[bool]': ...  # type: ignore

    def __neg__(self) -> '_ArrayLike[_S]': ...

    def __or__(self, value: Any) -> '_ArrayLike[_S]': ...

    def __pos__(self) -> '_ArrayLike[_S]': ...

    def __pow__(self, value: Any) -> '_ArrayLike[Any]': ...

    def __radd__(self, value: Any) -> '_ArrayLike[Any]': ...

    def __rand__(self, value: Any) -> '_ArrayLike[_S]': ...

    def __rdivmod__(self, value: Any) -> Tuple['_ArrayLike[int]', '_ArrayLike[float]']: ...

    def __rfloordiv__(self, value: Any) -> '_ArrayLike[Any]': ...

    def __rlshift__(self, value: Any) -> '_ArrayLike[Any]': ...

    def __rmatmul__(self, value: Any) -> '_ArrayLike[Any]': ...

    def __rmod__(self, value: Any) -> '_ArrayLike[Any]': ...

    def __rmul__(self, value: Any) -> '_ArrayLike[Any]': ...

    def __ror__(self, value: Any) -> '_ArrayLike[_S]': ...

    def __rpow__(self, value: Any) -> '_ArrayLike[Any]': ...

    def __rrshift__(self, value: Any) -> '_ArrayLike[Any]': ...

    def __rshift__(self, value: Any) -> '_ArrayLike[Any]': ...

    def __rsub__(self, value: Any) -> '_ArrayLike[Any]': ...

    def __rtruediv__(self, value: Any) -> '_ArrayLike[Any]': ...

    def __rxor__(self, value: Any) -> '_ArrayLike[_S]': ...

    def __setattr__(self, name: str, value: Any) -> None: ...

    def __setitem__(self, key: Any, value: Any) -> None: ...

    def __str__(self) -> str: ...

    def __sub__(self, value: Any) -> '_ArrayLike[Any]': ...

    def __truediv__(sel, value: Any) -> '_ArrayLike[Any]': ...

    def __xor__(self, value: Any) -> '_ArrayLike[_S]': ...

#
# numpy's scalar hierarchy (http://docs.scipy.org/doc/numpy/reference/arrays.scalars.html#scalars)
#

class generic(_ArrayLike[_S], Generic[_S]): ...
class bool_(generic[bool]): ...
bool8 = bool_
class object_(generic[Any]): ...
class number(generic[_S], Generic[_S]): ...
class integer(number[int]): ...
class signedinteger(integer): ...
class byte(signedinteger): ...
class short(signedinteger): ...
class intc(signedinteger): ...
class int_(signedinteger): ...
class longlong(signedinteger): ...
class int8(signedinteger): ...
class int16(signedinteger): ...
class int32(signedinteger): ...
class int64(signedinteger): ...
class unsignedinteger(integer): ...
class ubyte(unsignedinteger): ...
class ushort(unsignedinteger): ...
class uintc(unsignedinteger): ...
class uint(unsignedinteger): ...
class ulonglong(unsignedinteger): ...
class uint8(signedinteger): ...
class uint16(signedinteger): ...
class uint32(signedinteger): ...
class uint64(signedinteger): ...
class inexact(number[float]): ...
class floating(inexact): ...
class half(floating): ...
class single(floating): ...
class float_(floating): ...
class longfloat_(floating): ...
class float16(floating): ...
class float32(floating): ...
class float64(floating): ...
class float128(floating): ...
class complextfloating(inexact): ...
class csingle(complextfloating): ...
class complex_(complextfloating): ...
class clongfloat(complextfloating): ...
class complex64(complextfloating): ...
class complex128(complextfloating): ...
class complex256(complextfloating): ...
class flexible(generic[_S], Generic[_S]): ...
class character(flexible[str]): ...
class str_(character): ...
class unicode_(character): ...
class void(flexible[None]): ...

class ndarray(_ArrayLike[_S], Generic[_S]):
    """numpy.ndarray"""
    ctypes = None    # type: Any  # TODO Implement ctypes type hint

    # TODO Need to find a way to restrict buffer type
    def __init__(self, shape: Tuple[int, ...], dtype: Optional[DtypeType]=None,
                 buffer: Optional[Any]=None, offset: Optional[int]=None,
                 strides: Optional[Tuple[int, ...]]=None, order: Optional[str]=None) -> None: ...

#
# Array creation routines
#

def array(object: Any, dtype: Optional[Any]=None, copy: Optional[bool]=True,
          order: Optional[str]=None, subok: Optional[bool]=False,
          ndmin: Optional[int]=0) -> ndarray[Any]: ...
def asarray(a: Any, dtype: Optional[DtypeType]=None, order: Optional[str]=None) -> ndarray[Any]: ...
def asanyarray(a: Any, dtype: Optional[DtypeType]=None, order: Optional[str]=None) -> ndarray[Any]: ...  # TODO figure out a way to restrict the return type
def asmatrix(data: Any, dtype: Optional[DtypeType]=None) -> Any: ...  # TODO define matrix
def ascontiguousarray(a: Any, dtype: Optional[DtypeType]=None) -> ndarray[Any]: ...
def copy(a: Any, order: Optional[str]=None)	-> ndarray[Any]: ...
def empty(shape: ShapeType, dtype: Optional[DtypeType]=float, order: Optional[str]='C') -> ndarray[Any]: ...
def empty_like(a: Any, dtype: Optional[Any]=None, order: Optional[str]='K',
               subok: Optional[bool]=True) -> ndarray[Any]: ...
def eye(N: int, M: Optional[int]=None, k=0, dtype: Optional[DtypeType]=float) -> ndarray[Any]: ...

def frombuffer(buffer: Any, dtype: Optional[DtypeType]=float, count: Optional[int]=-1,  # TODO figure out a way to restrict buffer
               offset: Optional[int]=0) -> ndarray[Any]: ...
def fromfile(file: Any, dtype: Optional[DtypeType]=float, count: Optional[int]=-1,
             sep: Optional['str']='') -> ndarray[Any]: ...  # TODO fix file definition (There's a bug in mypy io's namespace https://github.com/python/mypy/issues/1462)
def full(shape: ShapeType, fill_value: Any, dtype: Optional[DtypeType]=None,
         order: Optional[str]='C') -> ndarray[Any]: ...
def full_like(a: Any, fill_value: Any, dtype: Optional[DtypeType]=None, order: Optional[str]='C',
              subok: Optional[bool]=True) -> ndarray[Any]: ...
def fromfunction(function: Callable[..., _S], shape: ShapeType, dtype: Optional[DtypeType]=float) -> ndarray[_S]: ...
def fromiter(iterable: Iterator[Any], dytpe: DtypeType, count: Optional[int]=-1) -> ndarray[Any]: ...
def fromstring(string: str, dtype: Optional[DtypeType]=float, count: Optional[int]=-1,
               sep: Optional[str]='') -> ndarray[Any]: ...
def identity(n: int, dtype: Optional[DtypeType]=None) -> ndarray[Any]: ...
def loadtxt(fname: Any, dtype: Optional[DtypeType]=float, comments: Optional[str]='#',
            delimiter: Optional[str]=None, converters: Optional[Dict[int, Callable[[Any], float]]]=None,
            skiprows: Optional[int]=0, usecols: Optional[Sequence[int]]=None,
            unpack: Optional[bool]=False, ndmin: Optional[int]=0) -> ndarray[float]: ...
def ones(shape: ShapeType, dtype: Optional[DtypeType]=float, order: Optional[str]='C') -> ndarray[Any]: ...
def ones_like(a: Any, dtype: Optional[Any]=None, order: Optional[str]='K',
              subok: Optional[bool]=True) -> ndarray[Any]: ...
def zeros(shape: ShapeType, dtype: Optional[DtypeType]=float, order: Optional[str]='C') -> ndarray[Any]: ...
def zeros_like(a: Any, dtype: Optional[Any]=None, order: Optional[str]='K',
               subok: Optional[bool]=True) -> ndarray[Any]: ...
