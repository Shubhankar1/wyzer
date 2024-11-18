from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/1')

@app.task(bind=True, max_retries=3)
def process_company(self, company_data):
    """
    Process a single company's financial and ESG data.
    """
    try:
        # Simulated processing logic
        result = f"Processed company: {company_data['name']}"
        return result
    except Exception as e:
        self.retry(exc=e)

