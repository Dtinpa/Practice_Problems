# Getting Started

## Installing IntelliJ
During the guided training we will be using IntelliJ, as that is our 
preferred go-to editor.

You do not _have_ to use IntelliJ for your editor if you don't want to.  
That statement comes with an understanding that if you use a different 
editor, you will get little / no support during the guided training.

I have tried Ensime a few times with Sublime, but haven't quite gotten
it figured out yet.

Download and install IntelliJ 15 Community Edition here (https://www.jetbrains.com/idea/download/)

Once you have it downloaded, install the Scala plugin.

## Install sbt
To work on the command line, you need to have sbt installed.

On a mac, you can simply do a `brew install sbt`

More information on installing on your workstation can be found here (http://www.scala-sbt.org/download.html)

## Install JDK
Make sure that you have JDK 1.8 installed.  Sure we can use other versions, but 
the guided training setup will use 1.8, and it's best if all workstations 
are consistent.

## Fork this repo
Fork this repo and clone it to your local workstation.

## Quick Build (installing the internet on your workstation)
*NOTE: before running this step, make sure that you are not on a Comcast network.  Comcast has some fun network filters that block certain scala dependencies.  I have not yet investigated why this is yet.  Best to do this step on Vendor Guest or another outside network*

Open a terminal and go to your newly cloned repo directory in *scala-training*.
From there run the following:

```
> sbt clean compile
```

Then sit back and wait for the internet to come down.

## Open the project in IntelliJ
This is easy, IntelliJ sbt support is great.  In IntelliJ, go to *File -> Open* and 
navigate to the directory for this project *scala-training* and open it!  Voila!

# SBT essentials
* *clean* - cleans the target directory
* *compile* - umm, compiles
* *test* - runs all unit tests
* *test-only *NameOfSpec* - runs an individual unit test

## repl fun times
You can start up the repl by going into sbt (just running `sbt` in the project directory)

Once in sbt, just type `console` to fire up the repl and it drops you into the scala console.

Type `"Hello World!" in the scala console, you will see output like: `res0: String = Hello World!`

Congrats, you are now a scala developer!  Here are some essentials:

### Quitting the console
*:q* quits the console

### Writing a multiline expression

```
scala> for(i < 1 to 3) {
     |   println(i)
     | }
```

### Paste Mode - free form programming in the console, yes your dreams just came true!
*:paste* enters paste mode, then you can just do some free form typing

```
scala> :paste

val name = "John"
val job = "Teacher"

println(name + " is a " + job)
```

When you are done writing your fun code, simply _Ctrl D_ to exit paste mode.

### Imports
You can use imports to make working in the repl simpler...

```
scala> import scala.concurrent.duration._
import scala.concurrent.duration._

scala> val oneSec = 1.second
oneSec: scala.concurrent.duration.FiniteDuration = 1 second
```





