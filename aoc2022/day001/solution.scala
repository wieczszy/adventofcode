@main def main =
    import scala.io.Source
    import scala.math.Ordering

    def solve1(inputfile: String): Int =
        val inn = Source.fromFile(inputfile).mkString
        val I = inn.split("\n\n").map(_.split("\n").map(_.toInt))
        val sums = I.map(_.sum)
        sums.max

    def solve2(inputfile: String): Int =
        val inn = Source.fromFile(inputfile).mkString
        val I = inn.split("\n\n").map(_.split("\n").map(_.toInt))
        val sums = I.map(_.sum).sorted(Ordering.Int.reverse)
        sums.take(3).sum

    val test = "test.txt"
    val input = "input.txt"

    println("-- TEST --")
    println(solve1(test))
    println(solve2(test))

    println("-- SOLUTION --")
    println(solve1(input))
    println(solve2(input))