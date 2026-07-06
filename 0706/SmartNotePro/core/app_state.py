"""
app_state.py

Smart Note Pro
전역 상태 관리 클래스
"""

class AppState:

    def __init__(self):

        # =========================
        # 파일 상태
        # =========================

        self.current_file = None
        self.is_saved = True

        # =========================
        # 에디터 상태
        # =========================

        self.zoom_level = 100
        self.word_wrap = True

        # =========================
        # 글꼴 상태
        # =========================

        self.font_name = "맑은 고딕"
        self.font_size = 14

        # =========================
        # UI 상태
        # =========================

        self.dark_mode = False

    # =========================
    # 상태 업데이트 함수
    # =========================

    def mark_dirty(self):
        """수정 상태"""
        self.is_saved = False

    def mark_saved(self):
        """저장 상태"""
        self.is_saved = True

    def set_file(self, path):
        """현재 파일 설정"""
        self.current_file = path