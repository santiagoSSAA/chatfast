class MockLLM:
    def generate_action_plan(self, input_data: str) -> str:
        # Simula la generación de un plan de acción
        return f"Generated action plan for: {input_data}"