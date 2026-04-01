class BrowserHistory:

    def __init__(self, homepage: str):
        self.backward = []
        self.f = []
        self.current = homepage

    def visit(self, url: str) -> None:
        if self.current:
            self.backward.append(self.current)

        self.current = url
        self.f= []

    def back(self, steps: int) -> str:

        for i in range(min(steps, len(self.backward))):
            self.f.append(self.current)
            self.current = self.backward.pop()

        return self.current

    def forward(self, steps: int) -> str:
        for i in range(min(steps, len(self.f))):
            self.backward.append(self.current)
            self.current = self.f.pop()

        return self.current
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)