
from app.db import SessionLocal,engine
from app.models import Player,Game
from sqlalchemy import select
import copy

new_board = [
    ['B',' ','B',' ','B',' ','B',' '],  # Row 0
    [' ','B',' ','B',' ','B',' ','B'],  # Row 1
    ['B',' ','B',' ','B',' ','B',' '],  # Row 2
    [' ',' ',' ',' ',' ',' ',' ',' '],  # Row 3
    [' ',' ',' ',' ',' ',' ',' ',' '],  # Row 4
    [' ','W',' ','W',' ','W',' ','W'],  # Row 5
    ['W',' ','W',' ','W',' ','W',' '],  # Row 6
    [' ','W',' ','W',' ','W',' ','W'],  # Row 7
   ]
    
black_moves={
        "move":[{"x":1,"y":1},{"x":-1,"y":1}],
        "capture":[{"x":2,"y":2},{"x":-2,"y":2}]
    }
white_moves={
        "move":[{"x":-1,"y":-1},{"x":1,"y":-1}],
        "capture":[{"x":-2,"y":-2},{"x":2,"y":-2}]
    }

class GamePlay ():

    

    def __init__(self):
        u_name=input("Enter user name: ")
        session=SessionLocal()
        self.session=session
        stmt=select(Player).where(Player.u_name==u_name)
        player=session.execute(stmt).scalar_one_or_none()

        #game
        if player==None:
            nick_name=input("Enter Nick Name: ")
            new_player=Player(u_name=u_name,nick_name=nick_name)
            session.add(new_player)
            session.commit()
            session.refresh(new_player)

            new_game=Game(player_id=new_player.id,board=new_board)
            session.add(new_game)
            session.commit()
            session.refresh(new_game)

            self.player=new_player
            self.game=new_game
          
            return
        stmt=select(Game).where(Game.player_id==player.id)
        game=session.execute(stmt).scalar_one_or_none()
        self.player=player
        self.game=game
        # self.print_board()
    
    def play_game(self):
        if self.game.is_white_turn: 
            self.human_play()
            return
        self.pc_play()

    def human_play(self):
        y_c=int(input("Enter x cordidantes: "))
        board=self.game.board
        if not isinstance(y_c,int):
            print("Invalid x cordindate")
            self.human_play()
            return
        
        if y_c>8 or  y_c<=0:
            print ("Invalid cordinate")
            print("Must be betweeen 1 and 8")
            self.human_play() 
            return
        
        x_c=int(input("Enter y cordidantes: "))

        if not isinstance(x_c,int):
            print("Invalid y cordindate")
            self.human_play()
            return
        
        if x_c>8 or  x_c<=0:
            print ("Invalid cordinate")
            print("Must be betweeen 1 and 8")
            self.human_play() 
            return
        
        x_c=x_c-1
        y_c=y_c-1

        piece=board[x_c][y_c]
        print(piece)
        if piece != "W":
            print(f"Invalid cordinate")
            print(f"No white piece at {x_c},{y_c}")
            self.human_play() 
            return
        
        moves=white_moves["move"]
        can_move=[]


        for move in moves:
            new_x=move["x"]+x_c
            new_y=move["y"]+y_c

            print("new x",new_x)
            print("new y",new_y)
            
            piece=board[new_x][new_y]
            print("piece at new position",piece)
            if piece==" " or piece=="X":
                board[new_x][new_y]="X"
                can_move.append({"x":new_y+1,"y":new_x+1,})
        
        print("You can move to the following positions")
        print(can_move)
        self.print_board()
        self.human_moves=can_move
        self.from_position={"x":x_c,"y":y_c}
        self.human_make_a_move()

    def human_make_a_move(self):
        y_c=int(input("Enter x cordidantes: "))
        board=self.game.board
        if not isinstance(y_c,int):
            print("Invalid x cordindate")
            self.human_play()
            return
        
        if y_c>8 or  y_c<=0:
            print ("Invalid cordinate")
            print("Must be betweeen 1 and 8")
            self.human_play() 
            return
        
        x_c=int(input("Enter y cordidantes: "))

        if not isinstance(x_c,int):
            print("Invalid y cordindate")
            self.human_play()
            return
        
        if x_c>8 or  x_c<=0:
            print ("Invalid cordinate")
            print("Must be betweeen 1 and 8")
            self.human_play() 
            return
        
        piece=board[x_c-1][y_c-1]
        if piece !="X":
            print("Invalid cordinate select a place with an X")
            self.human_make_a_move()
            return

        from_x=self.from_position["x"]
        from_y=self.from_position["y"]

        board[from_x][from_y]=" "
        board[x_c-1][y_c-1]="W"
        new_board=copy.deepcopy(board)
        self.game.board=new_board
        self.game.is_white_turn=False
        self.session.commit()
        self.session.refresh(self.game)
        print("move saved")

    def pc_play(self):
        pass

    def print_board(self):
        board=self.game.board

        for i, row in enumerate(board):

            s=" "+' | '.join(row)+" "
            print(f"{i+1} |{s}| ")
            print("-----------------------------------")
        print("  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")

game_play=GamePlay()
# print(vars(game_play.player))
# print(vars(game_play.game))

game_play.print_board()
game_play.play_game()