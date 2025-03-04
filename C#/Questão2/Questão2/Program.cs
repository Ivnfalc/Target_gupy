using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Console.Write("Informe um número: ");
        int numero = int.Parse(Console.ReadLine());

        if (BelongsToFibonacci(numero))
        {
            Console.WriteLine($"O número {numero} pertence à sequência de Fibonacci.");
        }
        else
        {
            Console.WriteLine($"O número {numero} não pertence à sequência de Fibonacci.");
        }
    }

    static List<int> FibonacciSequence(int n)
    {
        List<int> fibSequence = new List<int> { 0, 1 };
        while (fibSequence.Count < n)
        {
            int nextValue = fibSequence[fibSequence.Count - 1] + fibSequence[fibSequence.Count - 2];
            fibSequence.Add(nextValue);
        }
        return fibSequence;
    }

    static bool BelongsToFibonacci(int num)
    {
        List<int> fibSequence = FibonacciSequence(20); 
        return fibSequence.Contains(num);
    }
}
