# { "Depends": "py-genlayer:test" }

from genlayer import *

class AISourceClaimAuditor(gl.Contract):
    last_audit: str

    def __init__(self):
        self.last_audit = ""

    @gl.public.write
    def audit_claim(self, source_text: str, claim: str):
        input_data = f"""
SOURCE:
{source_text}

CLAIM:
{claim}
"""
        result = gl.eq_principle.prompt_non_comparative(
            lambda: input_data,
            task="Audit the claim using only the source text. Return: SUPPORTED, CONTRADICTED, or UNCLEAR with one short reason.",
            criteria="""
            The answer must be based only on the source text.
            The answer must start with SUPPORTED, CONTRADICTED, or UNCLEAR.
            The answer must include one short reason.
            The answer must not invent facts outside the source.
            """
        )
        self.last_audit = result

    @gl.public.view
    def get_last_audit(self) -> str:
        return self.last_audit
