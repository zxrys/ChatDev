"""Register built-in agent providers."""

from runtime.node.agent.providers.base import ProviderRegistry

ProviderRegistry.register(
    "openai",
    module_path="runtime.node.agent.providers.openai_provider",
    attr_name="OpenAIProvider",
    label="OpenAI",
    summary="OpenAI models via the official OpenAI SDK (responses API)",
)

ProviderRegistry.register(
    "gemini",
    module_path="runtime.node.agent.providers.gemini_provider",
    attr_name="GeminiProvider",
    label="Google Gemini",
    summary="Google Gemini models via google-genai",
)
