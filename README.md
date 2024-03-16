# rhythm-generator

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

### Rhythms: An Exhaustive Collection of Rhythms in Common Time
A compilation using randomly generated measures in 4/4. No rests, from whole notes to 16th notes. Effectively a prototype and proof of concept for what's to come.
- generator [source code](/src/gen_v1.py)
- digital copy on [GitHub](/books/rhythms-an-exhaustive-collection-of-rhythms-in-common-time.pdf) (gratis)
- paperback copy on [Amazon](https://www.amazon.com/dp/B0CVLH36QZ)

### Rhythms: Twenty-Thousand Measures in Common Time
Another experiment to understand the publishing process and mass scale measure generation.
- generator [source code](/src/gen_v1.py)
- digital copy on [GitHub](/books/rhythms-twenty-thousand-measures-in-common-time.pdf) (gratis)
- paperback copy on [Amazon](https://www.amazon.com/dp/B0CXM4H7YG)
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
