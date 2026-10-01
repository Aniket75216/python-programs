# Report generation polymorphism

class Report:
    def generate(self):
        pass


class PDFReport(Report):
    def generate(self):
        print("PDF report generated")


class ExcelReport(Report):
    def generate(self):
        print("Excel report generated")


class HTMLReport(Report):
    def generate(self):
        print("HTML report generated")


def create_report(report):
    report.generate()


for report in [PDFReport(), ExcelReport(), HTMLReport()]:
    create_report(report)\n