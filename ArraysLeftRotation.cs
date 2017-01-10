// https://www.hackerrank.com/challenges/ctci-array-left-rotation

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
class Solution {

    static void Main(String[] args) {
        string[] tokens_n = Console.ReadLine().Split(' ');
        int n = Convert.ToInt32(tokens_n[0]);
        int k = Convert.ToInt32(tokens_n[1]);
        string[] a_temp = Console.ReadLine().Split(' ');
        int[] a = Array.ConvertAll(a_temp,Int32.Parse);
        arrayIterate(a, k);        
        }
    
    static public void arrayIterate(int[] arr, int step){
        for (int i = step; i < arr.Length; i++)Console.Write(arr[i] + " ");
        for (int i = 0; i < step; i++)Console.Write(arr[i] + " ");
    }
    
}
