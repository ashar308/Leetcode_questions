#We need to check if there are 1's connected either vertical,horizontal 
#1 is land and 0 is water 
#Number of islands = ?

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        print(grid)
        #Number of rows
        rows = len(grid)
        print("Number of rows: ",{rows})
        #Number of colums
        columns = len(grid[0])
        print("Number of columns: ",{columns})
        def dfs(i,j):
            #if the adjacent one isnt 1 then we just return
            print("Entered DFS: ")

            if i>=rows or i<0 or j<0 or j>=columns or grid[i][j] !='1':
                return
            
            else:
                print("Entered else condition")
                grid[i][j] = '0'
                dfs(i,j-1)
                dfs(i,j+1)
                dfs(i+1,j)
                dfs(i-1,j)


        island = 0 
        for i in range(rows):
            print("i is ",{i})
            for j in range(columns):
                print("j is ",{j})
                #We are seeing if it is a one if there is even one one it is an islans

                if grid[i][j] == '1':
                    print("Entered the loop: when the if statement is true")
                    # we want the dfs to check for horizontal and vertical
                    #If we talk about ones that are horizontal that is 
                    #vertical : up, down so i-1,i+1
                    #Horizontal : -1, +1 and position is j so j-1 and j+1
                    island +=1
                    print("Number of islands are: ")
                    print(island)
                    dfs(i,j)
        return island

