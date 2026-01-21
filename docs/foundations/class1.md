
# Class 1

## Introductions

- Your Instructor

- [Students](https://github.com/UNH-HPC-2026/iam851/wiki/Students)

- [Syllabus](../syllabus/index.md)

- What you'll need for this class

  You'll need a computer to work on. Easiest is if you have a laptop you can
  bring to class. Otherwise, let me know so we can figure something out.

  High-Performance Computing is dominated by Linux. MacOS is essentially built
  on top of a UNIX environment, hence is pretty much interchangeable with Linux
  as far as this class goes. Windows is significantly different. If you're
  running Windows, I strongly recommend using
  [WSL2 (Windows Subsystem for Linux)](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode),
  which allows you to run Linux under Windows, and will give you that same
  environment as everyone else.

  An alternative might to be to use
  [Github Codespaces](https://education.github.com/experiences/primer_codespaces).

## Supercomputers

### At UNH:

* [UNH unveiling new (at the time) Cray supercomputer](http://boston.cbslocal.com/2013/11/03/unh-unveiling-new-cray-supercomputer-slated-for-physics-research/). Trillian was UNH's first Cray.

- UNH's maintains a "newer" Cray supercomputer, called
  ["Marvin"](https://plasma-use.sr.unh.edu/pmwiki.php?n=Main.Marvin) (a.k.a.
  "Plasma"). It has been
  [installed in 2020](https://www.usnh.edu/it/blog/2020/08/cray-supercomputer-major-research-instrumentation-mri-award).

- Research Computing Center at UNH:
  https://www.unh.edu/research/research-computing-center/areas-expertise

- Many groups have their own workstations / clusters.

## Sign up for github and the class

- Sign up for the class Discord at this
  [link](https://discord.gg/tDTuAMTA).

- Sign up for [github](https://github.com) (unless you already have a github
  account, you can just use that).

- Email [me](mailto:kai.germaschewski@unh.edu), so I can add you to the "github
  organization" (`UNH-HPC-2026`) for this class.

<!-- - [Sign up](https://classroom.github.com/a/uJaS1rtI) for the Github Classroom for this class. -->

## GitHub Wiki

In recent years, this class has used a GitHub Wiki to store the class materials, which is
a quick and easy way to put them up in a somewhat nicely formatted and organized way, and which makes it easy for anyone
(including you, the students) to edit them.

This year, I'm trying out using [sphinx](https://sphinx-doc.org) for the materials. Sphinx is a popular documentation generator, essentially the de-facto standard for many open-source projects, in particular those using Python. It does mean that editing isn't quite as simple as clicking the "Edit" button on a given Wiki page, but it's a useful tool to be familiar with, and it's still fairly easy to edit the documentation.

We will use GitHub a lot as we go, including me putting up sample code, and you using it to get / submit your coding assignments.

Across GitHub, there are a number of places that allow the user to write simple
text with a bit of added mark-up and have it formatted nicely, e.g., as
headlines, bullet lists, or to include code fragments. Example are bug reports ("Issues") or "Pull Requests", ie., requests to merge one's coding work into a project. Github Wikis also use this same format. Sphinx traditionally uses a different text format that serves the same purpose called ["ReStructured Text"](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html), but I've considered the Sphinx site you're looking at to use (almost) the same format that github uses, which is actually called `markdown`. `markdown` is one
flavor of a lightweight mark-up language, similar but not the same as used on wikipedia, as this one is more tailored towards coding. An overview of
the supported mark-up is available from
[GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

#### Your turn

You can look at the "source code" for a given page here by clicking on the "Invertocat" (the Github icon), then selecting "suggest an edit", which will take you to the corresponding file in the github repository where this site lives.

However, to keep things yet simpler, let's use an actual Github wiki to practice: https://github.com/UNH-HPC-2026/iam851/wiki

Create a new page about yourself. To do this, click the "New Page" button, then
use your name as the title and write something. After saving the page, navigate to the
[Students](https://github.com/UNH-HPC-2026/iam851/wiki/Students) page, edit it and add a link to the page you just created.
[As you'll find out, there's always many different ways to achieve the same
thing when it comes to computers. Alternatively, you can go to the Students page
first, create the link, and when you click on that link, github will ask whether
you want to create that new page for yourself.]

Eventually, your task is to make a page about yourself (or
something else -- this is on the public internet right now, so be aware of whatever you want to share), try out some of the formatting styles, and add a
picture or other external resource. As you'll use mark-down throughout the class, you'll frequently want to copy&paste code snippets or commands / error messages, so this is an opportunity to learn how to do so with proper formatting, too.

### Homework

- (next Tue) Finish the "Your Turn" / "In-class Exercise" assignments above. (This will always be part of a given class' homework, even if not explicitly stated.)

- (by next class) Make sure your account signups are all set.

- (next Tue) Go through this small first github classroom [assignment](https://classroom.github.com/a/uJaS1rtI) that introduces git and github.

- (by next class) Pick something you would like to learn about git or version control in general
  and do some research about it. Be prepared to write a couple of sentences
  about this topic next class.

<!-- - Create a wiki page about yourself (or your favorite animal / hobby /
  whatever). Use some markup and add a picture or something.

- Go through the first assignment from github classroom (t.b.d.) -->


## Additional Resources

- For further reading on High-Performance Computing, consider exploring the following resources:

    - [Introduction to High-Performance Computing](https://www.hpcwire.com/2021/01/12/a-beginners-guide-to-high-performance-computing/)
    
    - [Understanding Supercomputers](https://www.top500.org/lists/2021/11/)

- If you're interested in learning more about Linux, here are some helpful links:

    - [Linux Essentials](https://www.linuxfoundation.org/resources/what-is-linux/)

- Lastly, don't hesitate to reach out to your peers or instructor if you have questions or need assistance with any topics covered in class.
