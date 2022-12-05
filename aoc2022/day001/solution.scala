@main def main =
    import scala.io.Source
    import scala.math.Ordering

    def parseInput(inputfile: String): Array[Array[Int]] =
        val inn = Source.fromFile(inputfile).mkString
        inn.split("\n\n").map(_.split("\n").map(_.toInt))

    def solve1(inputfile: String): Int =
        val I = parseInput(inputfile)
        I.map(_.sum).max

    def solve2(inputfile: String): Int =
        val I = parseInput(inputfile)
        I.map(_.sum)
            .sorted(Ordering.Int.reverse)
            .take(3)
            .sum

    val test = "test.txt"
    val input = "input.txt"

    println("-- TEST --")
    println(solve1(test))
    println(solve2(test))

    println("-- SOLUTION --")
    println(solve1(input))
    println(solve2(input))