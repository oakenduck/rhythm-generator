# rhythm-generator

### How to Use:
```
$ git clone https://github.com/oakenduck/rhythm-generator
$ cd rhythm-generator/src
$ python rgen.py
```
```
-r, --rests        : bool     -> include rests
-v, --verbose      : bool     -> verbose output
-m, --meter        : int int  -> time signature
-o, --output       : file     -> output destination
-c, --count        : int      -> measures to generate
-s, --subdivision  : int      -> smallest subdivision
-t, --tuplet       : int...   -> tuplet types to include (unimplemented)
```

### Rhythms: An Exhaustive Collection of Rhythms in Common Time
A compilation using randomly generated measures in 4/4. No rests, from whole notes to 16th notes. Effectively a prototype and proof of concept for what's to come.
- generator [source code](/src/gen_v1.py)
- digital copy on [GitHub](/books/rhythms-an-exhaustive-collection-of-rhythms-in-common-time.pdf) (gratis)
- paperback copy on [Amazon](https://www.amazon.com/dp/B0CVLH36QZ)

---

## Goals:
- [x] separate mass measure generation from measure generator
- [ ] add lilypond support for instantiating notes
- [ ] add midi I/O
- [ ] add support for tuplets and dotted notes
- [x] combine rests that occur sequentially where appropriate
- [ ] design recursive measure generator for large-scale exhaustive search
