using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // Solicita ao usuário um número
        Console.Write("Informe um número: ");
        int numero = int.Parse(Console.ReadLine());

        // Verifica se o número pertence à sequência de Fibonacci
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
        // Gera a sequência de Fibonacci até o n-ésimo termo
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
        // Gerar a sequência de Fibonacci até um número suficientemente grande
        List<int> fibSequence = FibonacciSequence(20); // Você pode aumentar o limite se necessário
        return fibSequence.Contains(num);
    }
}