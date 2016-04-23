Swift Demangle
--------------

This is an IDA script to demangle Swift functions. It currently only works for ELF files. PRs are welcome for supporting other formats. The `swift-demangle` binary is required, it can be obtained from https://swift.org/download/.

Usage
-----

Load the `swift-demangle.py` script (Alt-F7), and choose the "Demangle swift functions" menu item in "Edit/Plugins". This will search the PLT for all Swift functions, demangle them, and add an anterior comments to the function calls:

![screenshot](https://raw.githubusercontent.com/gsingh93/ida-swift-demangle/master/screenshot.png)

TODO
----

- Support PE files
- Demangle global variables
- `swift-demangle` supports demangling multiple names at once, we should use this instead of invoking it for each name
