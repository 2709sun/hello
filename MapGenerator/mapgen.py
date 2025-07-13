import os
import tkinter as tk
from tkinter import simpledialog, messagebox

# 블록 픽셀 크기
TILE_W, TILE_H = 50, 50  # 변경된 타일 크기

# 블록 종류와 표시용 색상
BLOCK_TYPES = {
    "grass": "#5CAC2D",
    "dirt":  "#8B5A2B",
}

class RoomBuilder(tk.Frame):
    def __init__(self, master, rows, cols, room_name):
        super().__init__(master)
        self.rows = rows
        self.cols = cols
        self.room_name = room_name
        self.grid_cells = [[None] * cols for _ in range(rows)]
        self.cell_types = [[None] * cols for _ in range(rows)]

        # 현재 선택된 블록 타입 (기본: grass)
        self.current_type = tk.StringVar(value="grass")

        # 캔버스: 방 그리드
        self.canvas = tk.Canvas(
            self,
            width=cols * TILE_W,
            height=rows * TILE_H,
            bg="white"
        )
        self.canvas.pack(padx=10, pady=(10, 0))
        self._draw_grid()
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        # 블록 선택 UI
        sel_frame = tk.Frame(self)
        sel_frame.pack(pady=10)
        tk.Label(sel_frame, text="블록 종류:").pack(side="left")
        for btype in BLOCK_TYPES:
            rb = tk.Radiobutton(
                sel_frame, text=btype, value=btype,
                variable=self.current_type
            )
            rb.pack(side="left", padx=5)

        # 내보내기 버튼
        btn = tk.Button(self, text="내보내기", command=self.export)
        btn.pack(pady=(0, 10))

        self.pack()

    def _draw_grid(self):
        # 가로 줄 그리기
        for r in range(self.rows + 1):
            y = r * TILE_H
            self.canvas.create_line(0, y, self.cols * TILE_W, y, fill="#ccc")
        # 세로 줄 그리기
        for c in range(self.cols + 1):
            x = c * TILE_W
            self.canvas.create_line(x, 0, x, self.rows * TILE_H, fill="#ccc")

    def on_canvas_click(self, event):
        col = event.x // TILE_W
        row = event.y // TILE_H
        if 0 <= col < self.cols and 0 <= row < self.rows:
            selected = self.current_type.get()
            existing = self.cell_types[row][col]
            # 블록이 없으면 새로 배치
            if existing is None:
                x0 = col * TILE_W
                y0 = row * TILE_H
                rect = self.canvas.create_rectangle(
                    x0, y0,
                    x0 + TILE_W, y0 + TILE_H,
                    fill=BLOCK_TYPES[selected], outline=""
                )
                self.grid_cells[row][col] = rect
                self.cell_types[row][col] = selected
            # 동일한 종류 블록이면 제거
            elif existing == selected:
                self.canvas.delete(self.grid_cells[row][col])
                self.grid_cells[row][col] = None
                self.cell_types[row][col] = None
            # 다른 종류 블록이면 무시
            else:
                return

    def export(self):
        lines = []
        lines.append(f"class {self.room_name}(Room):")
        lines.append("    def __init__(self):")
        lines.append("        super().__init__()")
        lines.append("        self.blocks.add(")
        first = True
        for r in range(self.rows):
            for c in range(self.cols):
                btype = self.cell_types[r][c]
                if btype is not None:
                    x = c * TILE_W
                    y = r * TILE_H
                    comma = "," if first else ","
                    lines.append(f"            Block({x}, {y}, '{btype}'){comma}")
                    first = False
        lines.append("        )")

        filename = f"{self.room_name}.txt"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write("\n".join(lines))
            messagebox.showinfo("내보내기 완료", f"'{filename}' 파일이 생성되었습니다.")
        except Exception as e:
            messagebox.showerror("오류", f"파일 저장 중 오류가 발생했습니다:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    room_name = simpledialog.askstring("방 이름", "방 이름을 입력해주세요:")
    if not room_name:
        exit()

    size_str = simpledialog.askstring("방 크기", "방 크기를 입력해주세요 (rows cols):")
    if not size_str:
        exit()
    try:
        rows, cols = map(int, size_str.split())
    except:
        messagebox.showerror("입력 오류", "크기는 두 개의 정수로 입력해야 합니다.")
        exit()

    root.deiconify()
    root.title(f"Room Builder - {room_name}")
    app = RoomBuilder(root, rows, cols, room_name)
    root.mainloop()
