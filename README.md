# pants-ivy-example
An example pants install using a custom ivy config to support local consumption.

## Publishing locally
To publish the target in this repo into your local `~/.m2/repository` directory, you can run:

    ./pants publish.jar \
      --local=~/.m2/repository \
      --named-snapshot=`date +%s` \
      --no-dryrun \
      src/scala/org/pantsbuild/example

See `./pants help publish.jar` for more information on publishing options.

## Consuming locally
Because this repo configures an `ivysettings.xml` file with sbt and maven style local
repositories (and mentions that file in `pants.ini`), artifacts published to those
directories should be resolvable via the usual `jar_library` definitions.
