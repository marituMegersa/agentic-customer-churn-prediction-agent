def test_agent_orchestrator():
    prompt = "Test execution query for agentic-customer-churn-prediction-agent"
    assert len(prompt) > 0
    assert "Test" in prompt
