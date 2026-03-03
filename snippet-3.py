class ReportGenerator:
    def __init__(self, db):
        self.db = db

    def generate(self, report_type):
        users = self.db.query("SELECT * FROM users")
        if report_type == "summary":
            return self._summarize(users)
        elif report_type == "full":
            return self._generate_full_report(users)
        else:
            print("Invalid report type")

    def _summarize(self, users):
        return {"total": len(users)}

    def _generate_full_report(self, users):
        return users