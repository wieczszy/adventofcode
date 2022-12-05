@main def main =
    import scala.io.Source

    def solve1(inputfile: String): Int =
        var score = 0
        val bonus = Map(
            "X" -> 1,
            "Y" -> 2,
            "Z" -> 3
        )
        val results = Map(
            "A X" -> 3,
            "B X" -> 0,
            "C X" -> 6,
            "A Y" -> 6,
            "B Y" -> 3,
            "C Y" -> 0,
            "A Z" -> 0,
            "B Z" -> 6,
            "C Z" -> 3,
        )

        val lines = Source.fromFile(inputfile).getLines().toList

        lines.foreach { r =>
            val thirdChar = r.substring(2, 3)
            score = score + bonus(thirdChar) + results(r)
        }

        score

    def solve2(inputfile: String): Int =
        var score = 0
        val bonus = Map(
            "A" -> 1,
            "B" -> 2,
            "C" -> 3
        )
        val shape = Map(
            "A X" -> "C",
            "B X" -> "A",
            "C X" -> "B",
            "A Y" -> "A",
            "B Y" -> "B",
            "C Y" -> "C",
            "A Z" -> "B",
            "B Z" -> "C",
            "C Z" -> "A",
        )
        val result = Map("X" -> 0,"Y" -> 3, "Z" -> 6)

        val lines = Source.fromFile(inputfile).getLines().toList

        lines.foreach { r =>
            val thirdChar = r.substring(2, 3)
            score = score + bonus(shape(r)) + result(thirdChar)
        }

        score

    val test = "test.txt"
    val input = "input.txt"

    println("-- TEST --")
    println(solve1(test))
    println(solve2(test))

    println("-- SOLUTION --")
    println(solve1(input))
    println(solve2(input))