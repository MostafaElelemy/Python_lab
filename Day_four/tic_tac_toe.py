

import random
from typing import List, Optional, Tuple


class Board:
    """Encapsulates the 3x3 board state and related operations."""

    def __init__(self) -> None:
       
        self.__grid: List[List[str]] = [[" " for _ in range(3)] for _ in range(3)]

    def copy(self) -> "Board":
        b = Board()
        for r in range(3):
            for c in range(3):
                b.__grid[r][c] = self.__grid[r][c]
        return b

    def update(self, position: int, symbol: str) -> bool:
        """
        Update the board at a given position (1-9) with the symbol ('X' or 'O').
        Returns True if the move was successful, False otherwise.
        """
        if position < 1 or position > 9:
            return False
        row, col = self._pos_to_rc(position)
        if self.__grid[row][col] != " ":
            return False
        self.__grid[row][col] = symbol
        return True

    def is_full(self) -> bool:
        """Return True if the board has no empty spaces."""
        return all(cell != " " for row in self.__grid for cell in row)

    def check_winner(self) -> Optional[str]:
        """
        Check if there is a winner.
        Returns 'X', 'O' if someone won; None otherwise.
        """
        lines = []

       
        lines.extend(self.__grid)  # rows
        cols = [[self.__grid[r][c] for r in range(3)] for c in range(3)]
        lines.extend(cols)

        diag1 = [self.__grid[i][i] for i in range(3)]
        diag2 = [self.__grid[i][2 - i] for i in range(3)]
        lines.extend([diag1, diag2])

        for line in lines:
            if line[0] != " " and line.count(line[0]) == 3:
                return line[0]
        return None

    def available_moves(self) -> List[int]:
        """Return a list of available positions (1..9) that are empty."""
        moves = []
        for pos in range(1, 10):
            r, c = self._pos_to_rc(pos)
            if self.__grid[r][c] == " ":
                moves.append(pos)
        return moves

    @staticmethod
    def _pos_to_rc(position: int) -> Tuple[int, int]:
        """Convert 1..9 to (row, col)."""
        position -= 1
        return position // 3, position % 3

    def __str__(self) -> str:
        """Formatted board for display using the special method __str__."""
        
        lines = []
        for r in range(3):
            row_cells = []
            for c in range(3):
                cell = self.__grid[r][c]
               
                if cell == " ":
                    pos = r * 3 + c + 1
                    row_cells.append(str(pos))
                else:
                    row_cells.append(cell)
            lines.append(f" {row_cells[0]} | {row_cells[1]} | {row_cells[2]} ")
            if r < 2:
                lines.append("---+---+---")
        return "\n".join(lines)


class Player:
    """Base Player class (used for polymorphism)."""

    def __init__(self, name: str, symbol: str) -> None:
        self.name = name
        self.symbol = symbol  # 'X' or 'O'

    def make_move(self, board: Board) -> int:
        """
        Return chosen move (1..9). Implemented by subclasses.
        Should not update the board here; Game orchestrates that.
        """
        raise NotImplementedError


class HumanPlayer(Player):
    """Gets moves via terminal input with validation."""

    def make_move(self, board: Board) -> int:
        while True:
            try:
                raw = input(f"{self.name} ({self.symbol}), choose a position (1-9): ").strip()
                move = int(raw)
                if move not in range(1, 10):
                    print("Invalid choice: enter a number from 1 to 9.")
                    continue
                if move not in board.available_moves():
                    print("That spot is taken. Choose an empty cell.")
                    continue
                return move
            except ValueError:
                print("Invalid input: please enter a number (1-9).")


class ComputerPlayer(Player):
    """
    Simple strategy:
      1) If there is a winning move, take it.
      2) If opponent can win next, block it.
      3) Take center if free.
      4) Take a corner if free.
      5) Otherwise pick a random available move.
    """

    def make_move(self, board: Board) -> int:
      
        for move in board.available_moves():
            tmp = board.copy()
            tmp.update(move, self.symbol)
            if tmp.check_winner() == self.symbol:
                return move

        
        opponent = "O" if self.symbol == "X" else "X"
        for move in board.available_moves():
            tmp = board.copy()
            tmp.update(move, opponent)
            if tmp.check_winner() == opponent:
                return move

     
        if 5 in board.available_moves():
            return 5

       
        corners = [1, 3, 7, 9]
        random.shuffle(corners)
        for c in corners:
            if c in board.available_moves():
                return c

    
        return random.choice(board.available_moves())


class Game:
    """Coordinates players and board in a full game loop."""

    def __init__(self, player1: Player, player2: Player) -> None:
        self.players = [player1, player2]
        self.board = Board()
      
        self.current_turn = 0 if self.players[0].symbol == "X" else 1

    def switch_turns(self) -> None:
        self.current_turn = 1 - self.current_turn

    def play(self) -> None:
        print("\nWelcome to Tic-Tac-Toe!")
        print("Empty cells show their position number to help you choose.\n")
        while True:
            print(self.board)
            player = self.players[self.current_turn]

            move = player.make_move(self.board)
          
            self.board.update(move, player.symbol)

            winner = self.board.check_winner()
            if winner:
                print(self.board)
                name = next(p.name for p in self.players if p.symbol == winner)
                print(f"\n🎉 {name} wins as '{winner}'!")
                break

            if self.board.is_full():
                print(self.board)
                print("\nIt's a draw!")
                break

            self.switch_turns()


def choose_mode() -> int:
    while True:
        print("Choose mode:")
        print("  1) Play with a friend (Human vs Human)")
        print("  2) Play vs Computer (Human vs Computer)")
        choice = input("Enter 1 or 2: ").strip()
        if choice in {"1", "2"}:
            return int(choice)
        print("Invalid selection, try again.\n")


def main() -> None:
    mode = choose_mode()

    if mode == 1:
        name1 = input("Enter Player 1 name: ").strip() or "Player 1"
        name2 = input("Enter Player 2 name: ").strip() or "Player 2"
      
        p1 = HumanPlayer(name1, "X")
        p2 = HumanPlayer(name2, "O")
    else:
        name1 = input("Enter your name: ").strip() or "You"
        human_symbol = ""
        while human_symbol not in {"X", "O"}:
            human_symbol = input("Choose your symbol (X goes first) [X/O]: ").strip().upper()
            if human_symbol not in {"X", "O"}:
                print("Please enter X or O.")
        comp_symbol = "O" if human_symbol == "X" else "X"
        if human_symbol == "X":
            p1 = HumanPlayer(name1, "X")
            p2 = ComputerPlayer("Computer", "O")
        else:
            p1 = ComputerPlayer("Computer", "X")
            p2 = HumanPlayer(name1, "O")

    game = Game(p1, p2)
    game.play()


if __name__ == "__main__":
    main()
