# Class 2 - Version Management, Terminals, Editors


## Version management

Version control has been around for longer than computers, I'm pretty sure. But
it's become an increasingly more important (and fancier) topic as computers and
software have evolved.

Evolution of version management:

- copy `Thesis11.docx` to `Thesis12.docx`.
- copy `Thesis.docx` to `Thesis_2026_01_20.docx`.
- `sccs`/`rcs` (one file at a time; no networking)
- `cvs`/`svn` (changesets containing multiple files; centralized networking)
- `git` (distributed; also bitkeeper, mercurial, etc)

For those who care more about history:
* [talk on youtube](https://www.youtube.com/watch?v=W3hr-F8ie94)
* [punch cards](https://en.wikipedia.org/wiki/Computer_programming_in_the_punched_card_era)
* [Documentation](https://git-scm.com/doc) for `git`.

The main idea behind version control is to keep track of the history of, well,
anything. Most relevant for this class is, of course, managing code, but this
applies pretty much the same to keeping track of a thesis or a paper that's
being written, a website, documentation, engineering plans, etc.

Fundamentally, one saves the state of a file, a directory, or a whole project at
a given point in time in something that, in git terms, is called a "commit". For example, let's say you have three existing commits "A", "B", "C":

```{mermaid}
---
title: A simple linear history
---
gitGraph
   commit id: 'A'
   commit id: 'B'
   commit id: 'C'
```

Now, let's do some more work, and commit it, which creates version "D":

```{mermaid}
---
title: A simple linear history
---
gitGraph
   commit id: 'A'
   commit id: 'B'
   commit id: 'C'
   commit id: 'D'
```

`main` is the name of the default branch. In practice, it actually is a label
that points to the latest commit in a sequence -- and if one adds another
commit, it's automatically updated to point to the now-latest commit.

Things become more interesting as one starts using "branching", ie., working
with more than the one default branch. Branching is actually fairly
straight-forward, where it becomes more fun is when one wants to join branches back
together, ie., "merge". We'll get there...

```{mermaid}
---
title: Branching
---
gitGraph
   commit id: 'A'
   commit id: 'B'
   commit id: 'C'
   commit id: 'D'
   branch formatting
   branch spelling
   checkout formatting
   commit id: 'E'
   checkout spelling
   commit id: 'F'
   commit id: 'G'
```

### What is version management good for?

- managing versions
- sharing, allowing for customization
- work separately first, merge (or discard) later
- commit messages allow to more easily go back, understand history
- backup
- move code between machines
- supports team work
- automate processes

### What are problems?

- mess of versions


## Note on Integrated Development Environments (IDEs)

In the course of developing, testing and running code, one needs multiple pieces
of infrastructure:

- an _editor_ to write code / config files, etc.
- compilers
- debuggers
- version control
- a way to build the code
- a way to run code
- a way to analyze results
- a terminal to run commands
- a way to work on remote machines
- more "tooling" (formatter, static analyzers, linters, ...)

Traditionally, this would be all separate pieces, and there is certainly a
benefit to divide-and-conquer these aspects into separate, smaller building
blocks. But it is also quite nice and convenient to have this all under one
unified interface, and that's what IDEs (Integrated Development Environments)
like [Visual Studio Code](https://code.visualstudio.com/) do.

## Terminals / shells / command line

### Terminals

These days most, if not all, programs you interact with feature a GUI
(graphical user interface) front end. Back in the day, though, interacting with
programs via text only was state of the art, and this way of working hasn't died
yet (and I don't think it will anytime soon). In fact, people were quite happy
about the convenience that these interfaces brought about, much nicer than
carrying a stack of [punch cards](http://en.wikipedia.org/wiki/Punched_card) to
the machine room.

Initially, the terminals were actual
[teletypewriters(tty's)](http://en.wikipedia.org/wiki/Teletypewriter). and they
are still called this name today in UNIX/Linux. Things became even better with
the introduction of terminals like the
[VT100](http://en.wikipedia.org/wiki/VT100) that used monitors to display the
text. One could even do [ASCII art](http://en.wikipedia.org/wiki/ASCII_art). Last I checked, we
still had a VT220 terminal over at the RCC (Research Computing Center) in Morse
Hall, and I believe it is still used occasionally. Eventually, people started to build
text-based user interfaces (TUI), but those were quickly superseded by GUIs as
we know them today.

### Shells / command line

A shell is a program that takes care of basic interaction with the user, it
provides the command line interface you have already seen.

The primary function of a shell is to run programs, which as simple as typing
the name of the program, followed by options and arguments, if needed:

```
[kai@mbpro ~]$ whoami
kai
```

Shells also facilitate basic communication between multiple programs. There's a
lot of basic commands which can be called from the shell, a very non-exhaustive
list:

```
man who ls cd less cp mv rm echo cat tail bg fg jobs kill top grep wc du df sort
```

And other things:

```
. .. ~ dot-files
```

### Shell scripts

Often, it turns out one wants to do the same thing over and over again. One
thing that's actually quite useful is the "cursor up" key, which will let you go
back in your history of commands, so you don't have to type a command over
again. (There's also "Ctrl-R", for searching your history, which can be quite
useful, too.)

But if one has a set of commands one needs to repeat often, shell scripts are
useful. Essentially, those are just a text file with a bunch of commands, and
when you run the script, it behaves just as if you were typing all those
commands.

Here are some random real world examples:

This just saves me some typing when configuring my code. More importantly, I'll
inevitably have forgotten how I configured it two days later, so that helps
having a record of what I did.

```sh
kai@Kais-MacBook-Pro ~/src/psc/build-mac $ cat cmake.sh
CC=mpicc CXX=mpicxx FC=mpifort \
cmake \
    -DCMAKE_PREFIX_PATH=/Users/kai/src/ADIOS2/build-mac/install \
    -DCPM_gtensor_SOURCE=/Users/kai/src/gtensor \
    -DCMAKE_BUILD_TYPE=Debug \
    -DCMAKE_CXX_FLAGS_RELWITHDEBINFO="-g -O2" \
    -DPSC_USE_PERFETTO=OFF \
    -G Ninja \
    ..
```

A little helper to make it easier to auto-format Fortran files:

```sh
#! /bin/bash

for file in "$@"; do
    if [[ -f "$file" ]]; then
        echo "Formatting file: $file"
        cp $file $file.bak; findent < $file.bak > $file 
    else
        echo "Warning: $file is not a valid file."
    fi
done                                                                                                                                  
```


Another little helper script for comparing certain data in HDF5 files:

```sh
#! /bin/bash

if [ $# != 3 ]; then
  echo "Usage: h5diff-fld.sh <FILE1> <FILE2> <FLD>"
  exit 1
fi

FILE1=$1
FILE2=$2
FLD=$3

ID1=`h5ls -r $FILE1 | grep $FLD/p0/3d | cut -d ' ' -f 1`
ID2=`h5ls -r $FILE2 | grep $FLD/p0/3d | cut -d ' ' -f 1`
h5diff -p 1e-6 -v $FILE1 $FILE2 $ID1 $ID2
```

You can use scripts to save you typing similar things repeatedly. Here's
another example: Making a movie, though using a Makefile instead might have been
better:

```sh
#! /bin/bash

FIRST_FRAME=1
LAST_FRAME=119

python lim1.py
for a in `seq $FIRST_FRAME $LAST_FRAME`; do
    python plot.py data_$a.npy data_$a.png
done

ffmpeg -y -r 8 -i data_%d.png -r 30 -pix_fmt yuv420p lim1.mp4

rm -f *.png *.npy
```

A script is essentially just a text file with the commands you want to execute
-- and it should start with the first line shown above, which says which shell
to use to run the script. Even without that, you can always run a script by
saying, e.g., `bash make_movie.sh`. A useful trick for debugging is to call the
script with `bash -x make_movie.sh`, which will show the commands as they are
executed.

One should mark scripts as executable, so that they can be called like any other
program. You can do it by using the `chmod` command:

```sh
➜  ex_movie git:(main) ✗ ls -l make_movie.sh
-rw-------@ 1 kai  staff  234 Jan 20 19:25 make_movie.sh
➜  ex_movie git:(main) ✗ chmod a+x make_movie.sh
➜  ex_movie git:(main) ✗ ls -l make_movie.sh
-rwx--x--x@ 1 kai  staff  234 Jan 20 19:25 make_movie.sh
```

I put the movie example code into the syllabus repository:
[https://github.com/UNH-HPC-2026/iam851](https://github.com/UNH-HPC-2026/iam851).

A nice, and pretty comprehensive, introduction to shells and the commandline is
at [https://linuxcommand.org/](https://linuxcommand.org/). You don't need to know all of this for this class,
but learning the basics will help make your life easier in the future.

### Note - End of line encoding:

If bash scripts edited using windows apps are not producing correct file names
or don't work on Linux or WSL2, problem might be due to a difference in
character encoding used in windows editors ([End of line encoding - EOL](https://en.wikipedia.org/wiki/Newline)). In order to fix this just change the EOL
encoding from "Windows (CR LF)" to "Unix (LF)" and save the file. It is
typically in the bottom of the editor screen.

 <!-- (example screenshot - Notepad++). -->

### For Windows users: WSL2

I don't really have much experience with Windows Subsystem for Linux version 2
(WSL2) myself, but in theory it should work fairly well for what we need in this
class. Here is a tutorial on how to install WSL2 as a
[write-up](https://medium.com/@japheth.yates/the-complete-wsl2-gui-setup-2582828f4577),
and also a [youtube video](https://www.youtube.com/watch?v=X-DHaQLrBi8)
demonstrating how to do it. (Google has many other links, too).

My recommendation here is to install Ubuntu 24.04 as your linux
distribution, though that's also a fairly arbitrary choice. It's relatively
recent, quite stable, pretty popular, and supported for the long term. The links
above provide a way to install the graphical user interface (GUI) as well, which
I think will be helpful.

## Editors

If you want to write a program, or just about anything, you'll need a text
editor. Traditionally, in the UNIX world, there are two camps:
[vi](http://en.wikipedia.org/wiki/Vi) and
[Emacs](http://en.wikipedia.org/wiki/Emacs). These days, there are probably a
hundred text editors out there, and some of them are actually even
user-friendly.

There's always been some competition between using a dedicated editor together
with the command line vs an IDE (Integrated Development Environment). It's a
choice, but at this point my recommendation would be to try an IDE, but still
learn to use the command line, as that is fairly crucial when working on a
remote computer.

In recent years, Microsoft Visual Studio Code has become the most popular app in
this space -- it's free and (kinda) open-source. Other options would be
full-blown traditional IDEs (Visual Studio, Xcode, CodeBlocks, Eclipse), though
it is important to learn to develop code in a way where you can give it to
someone else who does not use the same IDE but will still be able to work with
your code.

## Building code

Once you start working on a computational project, you'll need to frequently
compile your code (unless you're using an interpreted language like python, then
you lucked out). It's helpful to compile code a lot during development, and even
more so while trying to find and fix the bugs...

The most basic way to get that done is to just call the compiler. My innovative
example program is in `hello.cxx`:

```c++
#include <cstdio>
#include <iostream>

int
main(int argc, char **argv)
{
  printf("Hi there.\n");

  // or if you prefer real C++
  std::cout << "Hi there from C++." << std::endl;

  return 0;
}
```

So you type:

```sh
[kai@mbpro hello]$ g++ hello.cxx -o hello
```

And it'll compile an executable `hello`, that you can run:

```sh
[kai@mbpro hello]$ ./hello
Hi there.
Hi there from C++.
```

#### Your turn

- Set up an environment that allows you to write code (editor/IDE), and work on
  the command line to call a compiler to compile your code.

- Create a source file `hello.cxx` which contains the code above, and compile
  and run it. (Feel free to do so in C or Fortran as well, but for a little
  while it'll makes sense to stick with C++ even if that's not your language of
  choice for the later part of the class.)

- Create a script `build.sh` that compiles the code, instead of you calling the
  compiler by hand

## Setting up your environment

Well, it is hard for me to give you specific instructions because there are so
many choices and preferences.

First of all, you do want to be able to work on the command line in a UNIX-like
environment. If you're working on Linux or Mac OS, that pretty much already
exists, so it's easiest to just use it.

On Windows, while it does have a built-in command line interface, it's
sufficiently different that it's not a good choice for what we want to learn in
the class. But there are some options:

The first option is to use WSL2, the Windows subsystem for Linux, which
essentially runs a Linux machine inside of Windows. When possible, that's quite
a good choice -- it might still cause some hassles, e.g., when it comes to
running graphical applications under Linux, but it'll do most of what we need
out of the box.

An alternative is to do the actual work on a remote Linux machine, and use your
local laptop or desktop just to log in and interact with that machine. This is
an option for any local operating system (Windows, Linux, Mac). It does need an
account on a remote machine -- and if that is your choice, I think we might as
well use marvin, the UNH Cray, even though it'll require a bit of work to set up
an account.

In terms of accessing a remote machine, the usual way to do it is ssh -- see
below. If your choice is to use VS Code as your editor / development
environment, it has a lot of capability built in that makes life easier when
working on a remote machine.

## Github codespaces

A newer, fancy way of getting a nice development environment is github
codespaces. What happens in this case is that the editor (essentially, VS code)
runs in your web browser, and the actual development happens on machine in the
cloud. This makes things very convenient in that you do not need to install
anything on your local machine, a web browser is all that is needed.

One drawback is that it's not (entirely) free. However, if you sign up as a
student, you should get a decent amount of monthly free usage (the class repo is
an education repo, this also might give you codespaces for free to some extent,
but the documentation isn't entirely clear on that.)

One of the drawbacks of github codespaces is that it makes you kinda overly
reliant on the cloud, you miss out on the experience of solving all the fun
problems that happen if one actually tries to do things on more typical local
and remote computers. So I think codespaces is a great way to get started, but
eventually, everyone should figure out what works best for them.

To give codespaces a try, go to [https://github.com/UNH-HPC-2026/iam851](https://github.com/UNH-HPC-2026/iam851), click on
the green `Code` button and select the `Codespaces` tab.
 
(homework)=
## Homework (due Tuesday before class)

- Finish reading the notes above. Not everything may make perfect sense, but try
  to get the main ideas -- and if you have questions, take note and ask them next class!

- Set up a working development environment, including the ability to

  - edit code
  - run commands on a UNIX/Linux command line
  - run a compiler, and run the resulting program

