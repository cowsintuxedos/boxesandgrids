# -*- coding: utf-8 -*-
"""
Created on Sun Feb 04 03:02:59 2018

@author: pushkar
"""

import pygame
import math
import time 
from copy import deepcopy
class BoxesGame():
    def __init__(self):
        #initialize variables for the current state
        self.hColor=[[0 for x in range(6)] for y in range(7)]
        self.vColor=[[0 for x in range(7)] for y in range(6)]
        self.boardh = [[False for x in range(6)] for y in range(7)]
        self.boardv = [[False for x in range(7)] for y in range(6)]
        #initialize variables for tracking the score
        self.score_player1=0;
        self.score_player2=0;
    def update(self):
    

        print 'Player 2'
        self.player2();
        print 'Player1'
        self.player1();
        
    # A function to lost all the possible moves 
    def list_possible_moves(self,state_h,state_v):
        #make the move true if the last move is not true to be true in the psuedo list
        
        next_moves=[];
        for x in range (7):
            for y in range(6):
                if(state_h[x][y]==False):
                    next_moves.append([x,y,1]); # append all horizontal moves
                
                
                
        for x in range (6):
            for y in range(7):
                if(state_v[x][y]==False):
                    next_moves.append([x,y,0]); # append all horizontal moves
                
        
                
        return next_moves
    # gives the current state of the system
    def current_state(self):
        '''
        h_matrix =[[False for x in range(6)] for y in range(7)];
        v_matrix=[[False for x in range(7)] for y in range(6)];
        for x in range (7):
            for y in range(6):
                h_matrix[x][y]=self.boardh[x][y]
        for x in range (6):
            for y in range(7):
                v_matrix[x][y]=self.boardv[x][y]
                
        '''
        h2=deepcopy(list(self.boardh))
        v2=deepcopy(list(self.boardv))
        return h2,v2
    #checks if the score has been updated by a given move or not
    def increment_score(self,move,h_matrix,v_matrix):
        temp_score=0;
        xpos=move[0];
        ypos=move[1];
        if(move[2]==0): # vertical matrices
            if(ypos==0):# left most edge
                if(h_matrix[xpos][ypos]==True and h_matrix[xpos+1][ypos]==True and v_matrix[xpos][ypos+1]==True):
                    temp_score=1;
            elif(ypos==6):# left most edge   
                if(h_matrix[xpos][ypos-1]==True and h_matrix[xpos+1][ypos-1]==True and v_matrix[xpos][ypos-1]==True):
                    temp_score=1;     
            else:
                if(h_matrix[xpos][ypos]==True and h_matrix[xpos+1][ypos]==True and v_matrix[xpos][ypos+1]==True):
                    temp_score=temp_score+1;
                if(h_matrix[xpos][ypos-1]==True and h_matrix[xpos+1][ypos-1]==True and v_matrix[xpos][ypos-1]==True):
                    temp_score=temp_score+1;
                    
        if(move[2]==1): # horizontal matrices
            if(xpos==0):
                if(v_matrix[xpos][ypos]==True and v_matrix[xpos][ypos+1]==True and h_matrix[xpos+1][ypos]==True):
                    temp_score=1;
            elif(xpos==6):
                if(v_matrix[xpos-1][ypos]==True and v_matrix[xpos-1][ypos+1]==True and h_matrix[xpos-1][ypos]==True):
                    temp_score=1;
                
            else:
                if(v_matrix[xpos][ypos]==True and v_matrix[xpos][ypos+1]==True and h_matrix[xpos+1][ypos]==True):
                    temp_score=temp_score+1;
                if(v_matrix[xpos-1][ypos]==True and v_matrix[xpos-1][ypos+1]==True and h_matrix[xpos-1][ypos]==True):
                    temp_score=temp_score+1;
                
                
            
        return temp_score;
    # function to actulally make a move
    def make_move(self,move,player_id):
        #print 'value before coming',self.boardh
        xpos=move[0];
        ypos=move[1];
        print xpos,ypos
        if(move[2]==1):# Vertical Matrices
            
            self.boardh[xpos][ypos]=True;
            
        if(move[2]==0):
            self.boardv[xpos][ypos]=True;
        #self.boardh_temp = self.boardh
        #self.boardv_temp = self.boardv
        score=self.increment_score(move,self.boardh,self.boardv);
        if(player_id==0):
            self.score_player1=self.score_player1+self.increment_score(move,self.boardh,self.boardv);
            
        if(player_id==1):
            self.score_player2=self.score_player2+self.increment_score(move,self.boardh,self.boardv);
        #ikimasu / delete later
        #print self.current_state()
            
       
        
    # function for printing the next state of the system    
    def next_state(self,move,h1,v1):
        xpos=move[0];
        ypos=move[1];
        h_matrix1=deepcopy(list(h1))
        v_matrix1=deepcopy(list(v1))
        
        
        score=self.increment_score(move,h_matrix1,v_matrix1);
        #ikimasu / delete later
        #print score;
        #print move[2];
        if(move[2]==0):#vetical matrices
            
            v_matrix1[xpos][ypos]=True;
            
            #self.boardv[xpos][ypos]=False
        if(move[2]==1):#horizontal matrices
            
            h_matrix1[xpos][ypos]=True;
            
            #self.boardh[xpos][ypos]=False
        #print move ,h_matrix,v_matrix
        return h_matrix1,v_matrix1,score;
    # function for 
    def game_ends(self,temp_h,temp_v):
        count=True;
        for x in range(6):
            for y in range(7):
                if not temp_h[y][x]:
                    count=False;
        for x in range(7):
            for y in range(6):
                if not temp_v[y][x]:
                    count=False;
        return count;
    def player1(self):
        temp_h=self.boardh
        temp_v=self.boardv
        
        next_move=self.list_possible_moves(temp_h,temp_v);
        #print self.boardh_temp,self.boardv_temp
        #print next_move

        #best_move=next_move[random.randint(0, len(next_move))-1]; #random movement
        #print 'before loop'
        
        best_move=next_move[0];
        best_score=0;
        for move in next_move:
            temp_h,temp_v,score=self.next_state(move,temp_h,temp_v);
            #print score
            if(score>best_score):
                best_score=score;
                best_move=move;
        
        #print 'Player 1  next moves', next_move_list
        #print 'Player 1  move made', next_move_list[0];
        self.make_move(best_move,0);
        print 'move made by player 1', best_move
        
        #if(make_move(next))
    def player2(self):
        '''
        Call the minimax/alpha-beta pruning  function to return the optimal move
        '''
        ## change the next line of minimax/ aplpha-beta pruning according to your input and output requirments
        temp_h=self.boardh
        temp_v=self.boardv

        moves = self.list_possible_moves(temp_h,temp_v)

        next_move=self.minimax(self.current_state(), 0); #minimax search
        next_move_alpha=self.alphabetapruning(self.current_state(), 1); #alpha-beta pruning version

        self.make_move(next_move,1)
        print 'move_made by player 2',next_move

    '''
    Write down the code for minimax to a certain depth do no implement minimax all the way to the final state. 
    '''

    def minimax(self, state, input_depth):
        # cutoff depth
        d = input_depth

        # unpacks h and v from input state
        cur_h,cur_v = state

        # setting up argmax
        def argmin(seq, fn):
            best = seq[0]; best_score = fn(best)
            for x in seq:
                x_score = fn(x)
                if x_score < best_score:
                    best, best_score = x, x_score
            return best

        def argmax(seq, fn):
            return argmin(seq, lambda x: -fn(x))

        # max value for player 2; s1 & s2 = player1 & player2 score deltas
        def max_value(h,v,depth,s1,s2):
            if depth > d or self.game_ends(h,v):
                return self.evaluate(h,v,s1,s2)

            next_moves = self.list_possible_moves(h,v)
            temp_value = float("-inf")
            for m in next_moves:
                next_h, next_v, next_score = self.next_state(m,h,v)
                temp_value = max(temp_value, min_value(next_h, next_v, depth+1, s1, s2-next_score))
            return temp_value

        # min value for player 1; s1 & s2 = player1 & player2 score deltas
        def min_value(h,v,depth,s1,s2):
            if depth > d or self.game_ends(h,v):
                return self.evaluate(h,v,s1,s2)

            next_moves = self.list_possible_moves(h,v)
            temp_value = float("inf")
            for m in next_moves:
                next_h, next_v, next_score = self.next_state(m,h,v)
                temp_value = min(temp_value, max_value(next_h, next_v, depth+1, s1+next_score, s2))
            return temp_value

        # unzips move to use min_value
        def get_min(m):
            next_h, next_v, score = self.next_state(m,cur_h,cur_v)
            return min_value(next_h, next_v, 0, 0, 0)
        
        best_move = argmax(self.list_possible_moves(cur_h,cur_v), lambda m: get_min(m))
        return best_move;
        
    '''
    Change the alpha beta pruning function to return the optimal move .
    '''    
    def alphabetapruning(self, state, input_depth):
        # cutoff depth
        d = input_depth

        # unpacks h and v from input state
        cur_h,cur_v = state

        # setting up argmax
        def argmin(seq, fn):
            best = seq[0]; best_score = fn(best)
            for x in seq:
                x_score = fn(x)
                if x_score < best_score:
                    best, best_score = x, x_score
            return best

        def argmax(seq, fn):
            return argmin(seq, lambda x: -fn(x))

        # max value for player2; s1 & s2 = player1 & player2 score deltas
        def max_value(state, alpha, beta, depth, s1, s2):
            h,v = state

            if depth > d or self.game_ends(h,v):
                return self.evaluate(h,v,s1,s2)

            next_moves = self.list_possible_moves(h,v)
            temp_value = float("-inf")
            for m in next_moves:
                next_h, next_v, next_score = self.next_state(m,h,v)
                temp_value = max(temp_value, min_value((next_h,next_v), alpha, beta, depth+1, s1, s2-next_score))
                if temp_value >= beta:
                    return temp_value
                alpha = max(alpha, temp_value)
            return temp_value

        # min value for player1; s1 & s2 = player1 & player2 score deltas
        def min_value(state, alpha, beta, depth, s1, s2):
            h,v = state

            if depth > d or self.game_ends(h,v):
                return self.evaluate(h,v,s1,s2)

            next_moves = self.list_possible_moves(h,v)
            temp_value = float("inf")
            for m in next_moves:
                next_h, next_v, next_score = self.next_state(m,h,v)
                temp_value = min(temp_value, max_value((next_h,next_v), alpha, beta, depth+1, s1+next_score, s2))
                if temp_value <= alpha:
                    return temp_value
                beta = min(beta, temp_value)
            return temp_value

        # unzips move to use min_value
        def get_min(m):
            next_h, next_v, next_score = self.next_state(m,cur_h,cur_v)
            return min_value((next_h,next_v), float("-inf"), float("inf"), 0, 0, 0)

        best_move = argmax(self.list_possible_moves(cur_h,cur_v), lambda m: get_min(m))
        #print "Best move: ",best_move
        #print "Best score: ",get_min(best_move)
        return best_move

    '''
    Write down you own evaluation strategy in the evaluation function 
    '''
    # assumes player is player2
    # calculates the optimal score delta difference and picks move based on that
    def evaluate(self, h, v, s1, s2): #s1 = player1 score delta, s2 = player2 score delta
        score = s2 - s1
        #print "Score delta: ",score
        return score
        
     
bg=BoxesGame();
while (bg.game_ends(bg.boardh,bg.boardv)==False):
    bg.update();
    print 'Player1 : score',bg.score_player1;
    print 'Player2 : score',bg.score_player2;
    #time.sleep(2)
print 'Player 2 wins' if bg.score_player2 >= bg.score_player1 else 'Player 1 wins'
#time.sleep(10)
pygame.quit()
