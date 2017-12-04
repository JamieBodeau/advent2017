// Jamie Bodeau

// Headers -----------------------------------------------

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
using namespace std;

#define N 100

// Prototypes --------------------------------------------

enum Direction{
    RIGHT = 0,
    UP    = 1,
    LEFT  = 2,
    DOWN  = 3
};

int adjTotal(int board[N][N], int row, int col){
    int total = 0;
    int modifiers[3] = {-1, 0, 1};
    
    // Check each location adjacent to the current spot
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            int adjRow = row + modifiers[i];
            int adjCol = col + modifiers[j];
            total += board[adjRow][adjCol];
        }
    }
    
    // Return the total of all adjacent cells, including self
    return total;
}

// Fills in a cell
void fillCell(int board[N][N], int row, int col){
    board[row][col] = adjTotal(board, row, col);
}

// Main Execution ----------------------------------------

int main(int argc, char** argv){
    
    // Create board
    int board[N][N] = {0};

    // Bookkeeping variables
    int level = 1;
    int r = N/2;
    int c = N/2;
    
    // Read input
    int input;
    cin >> input;
    printf("%d\n", input);

    // Fill first three cells
    
    board[r][c]     = 1;
    printf("%d %d %d\n", r, c, board[r][c]);
    board[r][++c]   = 1;
    printf("%d %d %d\n", r, c, board[r][c]);
    board[--r][c] = 2;
    printf("%d %d %d\n", r, c, board[r][c]);

    // This will track how many locations
    // we have filled in on this edge
    int edgesOnThisSize = 0;
    int edgeSize = 2;
    int spotsFilledInEdge = 0;
    Direction dir = LEFT;

    while (board[r][c] < input){
        // Check if we have finished our edge
        if (spotsFilledInEdge >= edgeSize){

            // Check if we need to increase the edge size
            edgesOnThisSize++;
            if (edgesOnThisSize % 2 == 0){
                edgesOnThisSize = 0;
                edgeSize++;
            }
            
            // Update the direction
            switch(dir){
                case RIGHT:
                    dir = UP;
                    break;
                case UP:
                    dir = LEFT;
                    break;
                case LEFT:
                    dir = DOWN;
                    break;
                case DOWN:
                    dir = RIGHT;
                    break;
            }

            // Reset variables
            spotsFilledInEdge = 0;
            
        }

        // Increment location based on direction
        switch(dir){
            case RIGHT:
                c++;
                break;
            case UP:
                r--;
                break;
            case LEFT:
                c--;
                break;
            case DOWN:
                r++;
                break;
        }

        // Fill spot
        fillCell(board, r, c);
        
        // Increment the number of spots we have filled in this edge
        spotsFilledInEdge++;

        printf("Row: %d   Col: %d   Val: %d\n", r, c, board[r][c]);

    }

    // Exit main
    return EXIT_SUCCESS;
}

// Functions ---------------------------------------------
