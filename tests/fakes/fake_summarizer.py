from core.base_summarizer import BaseSummarizer

class FakeSummarizer(BaseSummarizer):

    def __init__(self):
        self.called = False

    def summarize(self, messages):
        self.called = True
        return "This is a fake summary."