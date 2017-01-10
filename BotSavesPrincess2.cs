// https://www.hackerrank.com/challenges/saveprincess2

using System;
using System.Collections.Generic;
using System.IO;
class Solution {
    
static int[] findPlayer(String[] grid, string player)
{
    int[] playerlocation = new int[2];
    for(int row=0; row < grid.Length; row++)
    {
        int col = grid[row].IndexOf(player);
        if (col != -1)
        {
            playerlocation[0] = row;
            playerlocation[1] = col;
        }
    }
    return playerlocation;
}
    
static void nextMove(int n,int r, int c, String [] grid){
    int[] mario = findPlayer(grid, "m");
    int[] princess = findPlayer(grid, "p");
    int distanceVertical = mario[0] - princess[0];
    int distanceHorizontal = mario[1] - princess[1];
    if (distanceVertical > 0)
    {
        Console.WriteLine("UP");
    }
    else if (distanceVertical < 0)
    {
        Console.WriteLine("DOWN");
    }
    else if (distanceHorizontal < 0)
    {
        Console.WriteLine("RIGHT");
    }
    else if (distanceHorizontal > 0)
    {
        Console.WriteLine("LEFT");
    }
}
static void Main(String[] args) {
        int n;

        n = int.Parse(Console.ReadLine());
        String pos;
        pos = Console.ReadLine();
        String[] position = pos.Split(' ');
        int [] int_pos = new int[2];
        int_pos[0] = Convert.ToInt32(position[0]);
        int_pos[1] = Convert.ToInt32(position[1]);
        String[] grid  = new String[n];
        for(int i=0; i < n; i++) {
            grid[i] = Console.ReadLine(); 
        }

        nextMove(n, int_pos[0], int_pos[1], grid);

     }
}
