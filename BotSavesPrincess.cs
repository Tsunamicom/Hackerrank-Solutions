// https://www.hackerrank.com/challenges/saveprincess

using System;
using System.Collections.Generic;
using System.IO;
class Solution {
    
    static String[] getGrid()
    {
        int gridsize = int.Parse(Console.ReadLine());
        String[] grid = new String[gridsize];
        for(int i=0; i < gridsize; i++)
        {
            
            grid[i] = Console.ReadLine();
        }
        return grid;
    }
    
    static int[] locatePrincess(String[] grid)
    {
        int[] princessloc = new int[2];
        for(int row=0; row < grid.Length; row++)
        {
            int col = grid[row].IndexOf("p");
            if (col != -1)
            {
                princessloc[0] = row;
                princessloc[1] = col;
            }
        }
        return princessloc;
    }
    
    static int[] locateMario(String[] grid)
    {
        int[] marioloc = new int[2];
        for(int row=0; row < grid.Length; row++)
        {
            int col = grid[row].IndexOf("m");
            if (col != -1)
            {
                marioloc[0] = row;
                marioloc[1] = col;
            }
        }
        return marioloc;
    }

    static void saveThePrincess(String[] grid)
    {
        int[] princess = locatePrincess(grid);
        int[] mario = locateMario(grid);
        int distanceVertical = mario[0] - princess[0];
        int distanceHorizontal = mario[1] - princess[1];
        if(Math.Abs(distanceVertical) > 0)
        {
            for(int steps=0; steps < Math.Abs(distanceVertical); steps++)
            {
                if(distanceVertical < 0){Console.WriteLine("DOWN");}
                else{Console.WriteLine("UP");}
            }
        }
        if(Math.Abs(distanceHorizontal) > 0)
        {
            for(int steps=0; steps < Math.Abs(distanceHorizontal); steps++)
            {
                if(distanceHorizontal < 0){Console.WriteLine("RIGHT");}
                else{Console.WriteLine("LEFT");}
            }
        }
    }
    
    static void Main(String[] args)
    {
        saveThePrincess(getGrid());
    }
}
