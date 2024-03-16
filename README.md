# rhythm-generator

This tool has been used to generate literally millions of measures in arbitrary time signatures for my own entertainment and experiments. Some of these have resulted in documents existing as collections of them, which can be found in the [rhythm-books](https://github.com/oakenduck/rhythm-books) repository.

### Usage:
```
$ git clone https://github.com/oakenduck/rhythm-generator
$ cd rhythm-generator/src
$ python rgen.py
```
```
-r, --rests        :          -> include rests
-d, --dots         :          -> include dotted notes
-v, --verbose      :          -> verbose output
    --sorted       :          -> sort least to most notes per measure
-m, --meter        : int int  -> time signature
-o, --output       : file     -> output destination
-c, --count        : int      -> measures to generate
-s, --subdivision  : int      -> smallest subdivision
-t, --tuplet       : int...   -> tuplet types to include (unimplemented)
```

---

## Goals:
- [x] separate mass measure generation from measure generator
- [x] combine rests that occur sequentially where appropriate
- [ ] add support for tuplets and dotted notes
  - [x] dotted notes
  - [ ] tuplets
- [ ] support stem placement for complex odd meters
- [ ] add midi I/O
- [ ] add lilypond support for instantiating notes
- [ ] design recursive measure generator for large-scale exhaustive search
