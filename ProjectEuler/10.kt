/*
* first find prime numbers
* then calculate sum of prime number below 2 million
* */
fun main(args: Array<String>) {
    var Sum = 0
    for (number in 3..2000000 step 2)
    {
        var counter = 0
        for (i in 1..number/2)
        {
            if (number%i==0)
                counter++
        }
        counter++
        if (counter==2)
            Sum += number
        //println(number)
    }
    println(Sum+2)
}
