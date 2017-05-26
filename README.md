

# Client-side or library-side memory allocation with [Python CFFI](https://cffi.readthedocs.io)?

Client side is more general but we also wish a Pythonic API.
Check out [test.py]((../master/test.py).


## How to build and run the example

```
mkdir build
cd build
cmake ..
make
cd ..
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
EXAMPLE_BUILD_DIR=build python test.py
```
