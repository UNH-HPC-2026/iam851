# Class 3 - Writing and Organizing Code

## Today

- Today's github classroom [assignment](https://classroom.github.com/a/gPR3HIWN)

- The next couple of classes, we'll deal with organizing and building code --
  first manually, and then using tools like `make` and `cmake`. As we go, we'll
  start using version management in practice, too.

## Writing code

As I touched upon last time, a lot of time is spent in an editor where one can
do the actual code writing. That editor may be stand-alone, or it may be part of
a bigger Integrated Development Environment (IDE). That choice is yours. In
either case, you'll likely want to use an editor with a graphical user
interface.

Usually, it's easiest and preferable to run your editor on the machine you're
working on, ie., directly in Windows if you're on Windows, or on the Mac if
you're using a Mac, and same for Linux, too. There is the alternative of running
the editor on the system you're using for development (e.g., WSL2, or a remote Linux machine) and just have
the display happen on your host machine, though.

If the editor is not running on the same system where you compile and run the
code, there is a potential issue of keeping the code you're working on in sync.
Traditionally, one might edit the code on Windows, then copy it to Linux,
compile it there, find an error, edit on Windows again, copy again, etc., which
is painful. Most fancier editors actually allow to work on remote files in
various ways, which is a good option. For example, VS Code has various extensions like "Remote-SSH", "Dev Environments", "WSL", and those make it rather seamless to have the editor run on one system and have the development happen on another.

For WSL2 you might consider also the following:

On your host (Windows) system, you have the `C:` drive (and maybe `D:`). The
filesystem that Linux sees is a different one, but those windows drives get
"mounted" into Linux under `/mnt/c/` and `/mnt/d/`. So if you use your editor
the edit `C:\Users\abc\iam851\hello.cxx`, you'll find that very same file on
Linux in `/mnt/c/Users/abc/iam851/hello.cxx`. Note how conveniently (not!) one
is using backslashes and the other forward slashes.

Since those windows paths are a lot of typing in Linux, one can use a "symlink"
(symbolic link) to make things a bit easier:

```sh
$ ln -s /mnt/c/Users/abc/iam851 .
$ cd iam851 # much more convenient to type than "cd /mnt/c/Users/abc/iam851"
```

### Getting the starter code

In order to work with git repositories, the first step is to create one. There are fundamentally two approaches:
* Create a local repository first, and then push it to a remote place later (if ever, but I'd usually recommend it).
* Create a remote repository first, and then clone it onto your development system (e.g., your laptop).

First of all, what's a repository? Well, it's a structure where git keeps around all versions of your code (past and present), including metadata, like branches, tags, commit messages etc. Whether a repository is called "local" or "remote" is basically a question of perspective. From the perspective of your laptop, a repository that lives on github is remote, while one that is on your laptop's filesystem in `~/src/class-3-your-repo` is local. A repository that lives on UNH's Cray is remote from the perspective of your laptop, but after you log on to the Cray, it's local from that perspective.

#### Initializing a local repository

In this class, a lot of work will happen in github classroom assignment repositories, which are more or less just regular github repositories after signing up for them. Because of this, we'll usually use the second approach above, creating a remote repository first, and then cloning it onto your laptop. However, it's still useful to know how to create a local repository from scratch, so here's how to do it:

```sh
$ git init my-own-repo
$ cd my-own-repo
```

That's it -- you now have a local git repository in the `my-own-repo` directory and changed into it. You can check that by running

```sh
$ git status
```
which should show something like

```sh
On branch main
No commits yet
nothing to commit (create/copy files and use "git add" to track)
```

#### Cloning a remote repository

As stated above, in this class we'll usually start from a remote repository on
github. Signing up for the assignment will create such a repository for you. If you are not working on a class assignment but want to set up your own repository on github, you can do so by going to github.com, logging in, and clicking on the "New" button next to "Repositories" on your profile page.

While the content in your repo can be edited directly on github, that's generally not a feasible way to do actual code development (unless one uses something like github codespaces). So step 1 is to get the code to where you can work on it, which generally is going to be your laptop. Your assignment repo (repository) lives on github:

Repo: `https://github.com/unh-hpc-2026/class-3-your-repo`
```{mermaid}
gitGraph
   commit id: 'A'
   commit id: 'B'
   commit id: 'C'
```

In order to work on it on your laptop, you want to have that same repository
directly on your laptop. You do this by "cloning" it, for example by running
`git` on the command line:

```sh
$ git clone git@github.com:unh-hpc-2026/class-3-your-repo
```

In order to clone a remote repository, you need to know its URL. You can find that on the github page for your repository, by clicking on the green "Code" button, which will show you the URL to use for cloning. You can choose to clone via `https` or `ssh`. If you use `ssh`, you'll need to have set up ssh key-based authentication with github, which is described further below.

This will create a `class-3-your-repo` directory on your computer, which is an exact copy ("clone") of the whole
repository:

Repo: `/your/laptop/class-3-your-repo`
```{mermaid}
gitGraph
   commit id: 'A'
   commit id: 'B'
   commit id: 'C' tag:'main' tag:'origin/main'
```

As the command says, you now have a local "clone" of the github repository. As
such, it is originally identical to what's on github -- but they still are two
separate repositories. Right now the contain the same branches and the same
commits, but as you work on either of them, they will start to diverge and you
will have to make sure you sync them as needed. We'll get there.

Note: I indicated the duplicate nature of what's on your local laptop by indicating two branches, `main` and `origin/main`. (These are branches, though I had to use the "tag" visualization to show them here.) `main` is your local branch, while `origin/main` is a special name that git uses to refer to the `main` branch on the remote repository called `origin` (which is the default name git gives to the remote you cloned from). Initially, both branches point to the same commit, but as you work on either side, they will diverge.

#### Alternatives to running `git` on the command line:

- Most modern editors / IDEs have some git integration. For example, in VS Code
  you can hit cmd-shift-P (Mac) or ctrl-shift-P (Windows/Linux), type something
  like "clone", and you'll find the `Git: Clone` command there, which
  conveniently integrates with github as the place to clone from, and will help
  with getting authentication set up.

- There is the standalone "Github Desktop" application, which is a GUI
  specifically designed for developing locally while moving code back and forth
  to GitHub (via git).

- There are a bunch of standalone [git GUIs](https://git-scm.com/downloads/guis)
  as well.

### Authentication with github

Generally, cloning public repositories from github.com doesn't require any
authentication, ie., it should just work. However, your assignment repo is
private, and also in general, pushing code back to github requires you to be
authenticated to your userid.

If you use one of the GUI tools, they usually take care of authentication for
you, that is, they'll guide you through it. If you run `git` on the command
line, I advise to set up authentication via ssh, which is a good skill to have,
anyway, since it'll work the same for logging in to remote machines via ssh. See
[here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh),
for more details, and if you get stuckc, I'll be happy to help.

### Setting up github authentication with ssh

This follows the same principles as using ssh key-based authentication to log in
to remote machines. It requires some one-time set up, but should then just work
without you ever noticing what happens under the hood. Here are the steps to set
it up:

- generate a public-private keypair (if you have not done that before):

```sh
$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/kai/.ssh/id_rsa):
Created directory '/Users/kai/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /Users/kai/.ssh/id_rsa.
Your public key has been saved in /Users/kai/.ssh/id_rsa.pub.
```

[You need to hit Enter a couple of times to have it use the default locations.
Your ssh may default to different kinds of keys (not RSA), so the filenames may
differ.]

Note: Your private key will be stored on your laptop (or whereever you run the
command), and will never leave that system. However, if someone gets access to
your laptop, they can steal the key and then pretend to be you. It is safer to
choose a passphrase to encrypt the key, but that also means that you then have
to enter the passphrase every time the key is needed, or use `ssh-agent` to make
that less disruptive.

- Take the public key and register it in your github acccount. In order to do
  so, log into github.com, then click on your avatar in the top right corner,
  choose `Settings` and then `SSH and GPG keys`. Add a new SSH key -- give it a
  name, and copy & paste the content of the public key file
  (`/Users/kai/.ssh/id_rsa.pub` in my case). That should be it.

### Setting up github authentication via https

[I have little experience with this. There's nothing fundamentally better or worse
about doing it this way, though my experience is that ssh just works after the initial setup, while the https authentication can sometimes be a bit more cumbersome]. You can follow the instructions here:
<https://docs.github.com/en/get-started/getting-started-with-git/caching-your-github-credentials-in-git>

I have used the `gh` CLI tool before. It can be a useful quick way to do lots of stuff with github from the command line, and it worked relatively straightforwardly,
but generally my preferred way is to either go through my IDE, or to just go to
github.com on the web to handle pull requests etc.

#### Your turn

- Sign up for the class 3 github classroom assignment if you haven't done so
  already.

- Clone your assignment repository onto your laptop.

- Add a simple `hello.cxx` file that prints a message to the console. (See [](class2).)

- Compile and run it on your laptop to make sure it works.

- Commit and push your code to github.

Making a commit using `git` on the command line is a two-step process:
- First you stage the changes/files that you want to become part of the commit, e.g., `git add hello.cxx` to stage the new file you just created for the upcoming commit.
- Second, run `git commit -m "added hello.cxx"` to create the commit. In this case, I used the `-m` option to provide a commit message on the command line. Alternatively, you can just run `git commit`, which will open an editor for you to enter the commit message.

At this point, this is what your local repository looks like:

```{mermaid}
gitGraph
   commit id: 'A'
   commit id: 'B'
   commit id: 'C' tag:'origin/main'
   commit id: 'D' tag:'main'
```

The new commit `D` is only in your local repository. In order to make it available on github, you need to push it:

```sh
$ git push origin main # or simply "git push"
```

This takes the local `main` branch and pushes it to the remote repository called `origin` (which is the default name git gives to the remote you cloned from).

Now the local and remote repositories are back in sync:

```{mermaid}
gitGraph
   commit id: 'A'
   commit id: 'B'
   commit id: 'C'
   commit id: 'D' tag:'main' tag:'origin/main'
```

I'd say it certainly doesn't hurt to have some experience doing this on the command line, but as stated above, most people will probably find it more convenient to use their IDE or a GUI tool for day-to-day work. VS Code has version management built in, and you can find the relevant commands in the left-hand sidebar (the icon that looks like a branch with a dot on it). Staging files is done by clicking the `+` next to the file, committing is done by entering a commit message and clicking the checkmark icon, and pushing/pulling can typically be done by clicking the "Sync" button that appears in the bottom left corner when there are changes to push or pull.

#### Be careful when making commits

A commit is permanent (unless you do some advanced git surgery), so make sure that your commit only contains changes that belong together, and that your commit message
adequately describes what the commit does. Commits are what you see when you look back at your own history, and it's what other people see who are reviewing your code contributions or try to understand what you did. As such, it's worth spending a bit of time to make sure your commits are well structured and documented.

Specifically, don't just stage and commit everything you changed since the last commit. Instead, think about what logical changes you made, and make one commit per logical change. Staging time is where you want to look at and review what changes you're about to commit. For example, if you fixed a bug and added a new feature, those should be two separate commits, each with an appropriate commit message. Generally, you want to avoid committing things that are meant to be temporary, like debugging code or print statements you added to figure out a problem. You also don't want to add files that don't belong in the repository, like compiled binaries, editor backup files, etc. More about that later, but generally, if you didn't use your editor to create or modify a file, think twice before committing it.

## Building code

Once you start working on a computational project, you'll need to frequently
compile your code (unless you're using an interpreted language like Python, then
you lucked out). During development, and even more so while trying to find and
fix the bugs...

The most basic way to get that done is to just call the compiler by hand, as
you've seen in the last class. Slightly more sophisticated is to have a script
that takes care of calling the compiler.

### Using a script to build the code

Let's create a
little `build.sh` script -- for two reasons: First, because that way I can add
it to the code repository, so that I have a record of how I compiled the code.
But also, the commands to build the code are going to become more
complex, so it's not fun to keep typing them on the command line -- and even
worse, I may have forgotten how to do it by next week. Having it in a script
means that you not only can look at it and remind yourself, you can also just
run the script and don't care how it's done.

My `build.sh` file looks like this:

```sh
#! /bin/bash

g++ hello.cxx -o hello
```

Again, there's a number of ways to run the script. You can just say

```sh
[kai@mbpro hello4]$ bash build.sh
```

which tells the shell `bash` to run the script `build.sh`. An advantage of doing
it this way is that you can add the option `-x`: `bash -x build.sh` to see
what's happening.

In general, it's a good habit to mark scripts as executable, like compiled
programs are. Then they can be run just like any other program:

```
[kai@mbpro hello4]$ chmod a+x build.sh # mark as executable
[kai@mbpro hello4]$ ./build.sh # from now on, we can just run it like this
```

## A "real" app

Alright, maybe the simple hello world program is not actually a realistic
example of a complex real application. So let's do this in `class3/hello.c`:
(Since this is a new "application", and I don't want to get confused with my
existing one, I'm doing this in an new subdirectory `class3/`.) 

```c
#include <stdio.h>

void
greeting(void)
{
  printf("Hi there.\n");
}

int
factorial(int n)
{
  int i;
  int retval = 1;

  for (i = 1; i <= n; i++) {
    retval *= i;
  }

  return retval;
}

int
main(int argc, char **argv)
{
  greeting();

  printf("10 factorial is %d\n", factorial(10));
}
```

Um, still not a real application? Well, it'll have to do for now. This isn't
about coding, it's about organizing / building code, so I intentionally keep the
code itself simple. I also switched back to C for now, for a particular reason.
We can break this program up, and demonstrate what happens when building a more
complicated project.

### Your turn

- Create a new directory `class3/` in your assignment repository.

- Add the above `hello.c` file into that directory.

- Add a `build.sh` script to build this code.

- Compile and run the code using `build.sh` to make sure it works.

  Keep around the output of the program, so that you can copy&paste it into your
  assignment submission later.  

- Make a commit and push your changes to github.

## Separating out the `greeting()` function

So let's just use our imagination, let's say this file has became way too large
and we want to split it up. I'll pull out the `greeting()` function, you'll get
to do `factorial()`. The goal is to put the `greeting()` function into a new
file `greeting.c`:

```c
#include <stdio.h>

void
greeting(void)
{
  printf("Hi there.\n");
}
```

The `main` function remains in `hello.c`. This isn't quite perfect yet. But
first, let's see how to actually build this program.

## Compilers

It's worth mentioning that there are many C/C++ compilers out there, and I've
just used `gcc`/`g++`. These are the GNU C/C++ compilers, they are the most well
known open source compilers. In recent years, the clang/llvm compiler
infrastructure has also become popular -- you can use them (if they are
installed) by calling `clang`/`clang++`.

There also many other compilers available, e.g., from Intel, Cray, PGI, etc.
They do basically the same thing, but there are often noticable differences in
how to call them, what kinds of feature they support, how well they optimize,
etc.

The Fortran landscape is somewhat similar -- there is `gfortran` as part of the
GNU compiler suite. There is `flang` as part of clang/llvm. I don't personally
have experience with it, but from what I've heard I'm not sure it's ready for
primetime. There are a lot of vendor-supported proprietary compilers, like from
Intel, Cray, PGI / Nvidia, which tend to be pretty good, but they are not
necessarily free and don't work everywhere, so I'd recommend focusing on
gfortran.

## Adapting the build script

To compile the project, I'll now have to go through some more effort, or at
least I should. So let's work on a `build.sh` again. (I have not added a
`build.sh` to the github repository -- this will be part of "your turn")

My original `build.sh` file looked like this:

```sh
#! /bin/bash

gcc hello.c -o hello
```

Now that my source code is spread amongst two source files, I need to
tell the compiler. The easiest way is to say

```sh
#! /bin/bash

gcc hello.c greeting.c -o hello
```

Actually, that's just shorthand for telling the `gcc` to compile `hello.c`, then
compile `greeting.c`, then link the resulting object files together into an
executable called `hello`.

So what really happens is the following, and I prefer to be explicit about it,
in particular because it'll help understand where we're going with using
Makefiles.

```sh
#! /bin/bash

gcc -c hello.c
gcc -c greeting.c
gcc hello.o greeting.o -o hello
```

## Header files

Maybe you already got a warning like this from the compiler:

```sh
[kai@macbook hello (class-3)]$ ./build.sh
hello.c:20:3: warning: implicit declaration of function 'greeting' is invalid in C99
      [-Wimplicit-function-declaration]
  greeting();
  ^
1 warning generated.
```

Warnings are not errors, that is, the compiler will keep on going, but what the
compiler really means is "while this is technically acceptable, I think you may
have made a mistake here". And most of the time, the compiler is right, and you
should fix things.

### The `-Wall` compiler flag

I'll actually change one more thing, I'll add `-Wall` as a compiler flag. This
tells the compiler to turn on (almost) all warnings, and these warnings are
useful in finding problems in your code. If you hadn't already gotten the
warning above anyway, you should definitely see it now.

```
#! /bin/bash

gcc -Wall -c hello.c
gcc -Wall -c greeting.c
gcc hello.o greeting.o -o hello
```

### Fixing the warning

The issue is that we're now calling the `greeting()` function from `hello.c`,
but the compiler doesn't know anything about it, because it's now defined in
`greeting.c`. It's legal (and useful) to define functions in separate source
files, but one should at least tell the compiler that the function exists before
calling it. Technically, one should at least "declare" the function before using
it.

We'll do that in what's called a "header file". Here's `hello.h`:

```c

#ifndef HELLO_H
#define HELLO_H

void greeting(void);

#endif

```

The greeting function is now declared in `hello.h`, which doesn't quite help
yet, because we need to know that declaration when compiling `hello.c`. But now
that we have it in the header, we can include it there:

```diff
diff --git a/hello/hello.c b/hello/hello.c
index 4272def..ddf0bd8 100644
--- a/hello/hello.c
+++ b/hello/hello.c
@@ -1,4 +1,6 @@

+#include "hello.h"
+
 #include <stdio.h>

 int
```

### Not quite perfect yet

There are no more warnings, but there's still an issue that should be avoided:

Say I find my code being just a bit too boring and simple, so I want to
personalize my greeting:

```diff
diff --git a/hello/greeting.c b/hello/greeting.c
index 2adcc82..b62a9f1 100644
--- a/hello/greeting.c
+++ b/hello/greeting.c
@@ -2,7 +2,7 @@
 #include <stdio.h>

 void
-greeting(void)
+greeting(const char *name)
 {
-  printf("Hi there.\n");
+  printf("Hi there, %s!\n", name);
 }

```

What happens when we compile and run the code now? Why?

#### Your turn

- Follow the steps above, ie., start with a single `hello.c`, make a build
  script, and then split off `greeting.c`, etc.

- Make the change to the greeting function above. What happens? Why? What can
  you do about it, and how could you avoid this happening in the first place?

- Separate out the `factorial()` function into its own file `factorial.c`, and
  adapt `build.sh` accordingly. Make sure everything still compiles and runs
  correctly.

- Finally, redo all of this using C++, starting from scratch in a new
  subdirectory. In particular, start over with `hello.cxx`, and generally, make
  your source files have the `.cxx` extension. (Some people like to use `.hxx`
  for C++ header files, though most, like me, still use `.h`. That's up to you.)

  For some additional fun, you can change the output to using `<iostream>` along
  the way.

  More importantly, though, what changes when you follow the same process in
  C++? Any idea why?

## Homework

- Complete the above "your turn" tasks. Make commits as you go, and make sure you keep notes. It is useful to cut&paste what you
did, and what happened, in particular errors or surprising results. You may not
always be able to answer the "why" for sure, but you can at least speculate.


