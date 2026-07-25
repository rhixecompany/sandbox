# Crypto Wallet API Evaluation Patterns

## Provider Comparison Matrix

| Provider | Custody Model | Chains | SDKs | Webhooks | Compliance |
|----------|--------------|--------|------|----------|------------|
| Cobo | MPC/WaaS | 50+ | Python, JS, Go | Yes | SOC2, ISO27001 |
| Fireblocks | MPC | 30+ | JS, Python | Yes | SOC2, ISO27001 |
| BitGo | Multi-sig/MPC | 100+ | JS, Java | Yes | SOC2 |
| Coinbase Cloud | Custodial | 10+ | JS, Python | Yes | Regulated |

## Evaluation Checklist

- [ ] Custody model matches requirements
- [ ] All target chains supported
- [ ] Sandbox environment available
- [ ] Security audit passed
- [ ] Compliance requirements met
- [ ] Webhook reliability tested
- [ ] Rate limits acceptable
- [ ] Support SLA defined

## Integration Patterns

```python
# Universal wallet interface
class WalletProvider:
    async def create_wallet(self, chain: str) -> Wallet: ...
    async def get_address(self, wallet_id: str, chain: str) -> str: ...
    async def get_balance(self, wallet_id: str, chain: str, token: str = None) -> Balance: ...
    async def send_transaction(self, wallet_id: str, to: str, amount: str, chain: str) -> Tx: ...
    async def estimate_fee(self, wallet_id: str, to: str, amount: str, chain: str) -> Fee: ...

# Factory pattern for multi-provider
class WalletFactory:
    def __init__(self):
        self.providers = {}
    
    def register(self, name: str, provider: WalletProvider):
        self.providers[name] = provider
    
    def get(self, name: str) -> WalletProvider:
        return self.providers[name]
```

## Security Requirements

1. **Key Management**: Never log API keys, use secret managers
2. **Idempotency**: Use idempotency keys for all mutations
3. **Webhook Verification**: Always verify signatures
4. **Rate Limiting**: Implement exponential backoff
5. **Audit Logging**: Log all wallet operations