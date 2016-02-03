package org.pantsbuild.example

object Example {
  def main(args: Array[String]) {
    println(s"Got: ${args.mkString("\n  ", "\n  ", "")}")
  }
}
