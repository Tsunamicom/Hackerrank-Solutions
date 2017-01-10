// https://www.hackerrank.com/challenges/ctci-bubble-sort

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
class Solution {

    static void Main(String[] args) {
        int n = Convert.ToInt32(Console.ReadLine());
        string[] a_temp = Console.ReadLine().Split(' ');
        int[] a = Array.ConvertAll(a_temp,Int32.Parse);
        bubblesort(a);
    }
    static void bubblesort(int[] a){
        int totalSwaps = 0;
        
        for (int i = 0; i < a.Length; i++) {
            // Track number of elements swapped during a single array traversal
            int numberOfSwaps = 0;
    
            for (int j = 0; j < a.Length - 1; j++) {
            // Swap adjacent elements if they are in decreasing order
                if (a[j] > a[j + 1]) {
                    int temp = a[j];
                    a[j] = a[j+1];
                    a[j+1] = temp;
                    numberOfSwaps++;
                }
            }

            // If no elements were swapped during a traversal, array is sorted
            if (numberOfSwaps == 0) {
                break;
            }
            totalSwaps += numberOfSwaps;
        }
        
        Console.WriteLine("Array is sorted in {0} swaps.", totalSwaps);
        Console.WriteLine("First Element: {0}", a[0]);
        Console.WriteLine("Last Element: {0}", a[a.Length-1]);
        
    }
}
