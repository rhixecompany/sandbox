# Instructions Redaction Report

Generated: 2026-08-15T17:00:59+01:00

This report lists instruction files that contain conservative redaction placeholders (<REDACTED_*>) introduced by the auto-fix tool. These files were copied into `docs/instructions/` in the repository. Human review is required to confirm or replace placeholders.

Summary:

- Files with redactions: 19
- Total matches found: 37

Files and excerpts (line numbers indicate the original external file):

1. ansible.instructions.md (line 27)
   - Use the `ansible.builtin` collection for [builtin modules and plugins](https://docs.ansible.<REDACTED_BLOB>.html#plugin-index)

2. azure-verified-modules-bicep.instructions.md (lines 22-23)
   - **Bicep Resource Modules**: `https://raw.githubusercontent.com/Azure/Azure-Verified-<REDACTED_BLOB>-indexes/BicepResourceModules.csv`
   - **Bicep Pattern Modules**: `https://raw.githubusercontent.com/Azure/Azure-Verified-<REDACTED_BLOB>-indexes/BicepPatternModules.csv`

3. azure-verified-modules-terraform.instructions.md (lines 38-40)
   - **Terraform Resource Modules**: `https://raw.githubusercontent.com/Azure/Azure-Verified-<REDACTED_BLOB>-indexes/TerraformResourceModules.csv`
   - **Terraform Pattern Modules**: `https://raw.githubusercontent.com/Azure/Azure-Verified-<REDACTED_BLOB>-indexes/TerraformPatternModules.csv`
   - **Terraform Utility Modules**: `https://raw.githubusercontent.com/Azure/Azure-Verified-<REDACTED_BLOB>-indexes/TerraformUtilityModules.csv`

4. code-review-generic.instructions.md (lines 155, 406, 415)
   - const API_KEY: <REDACTED_PLACEHOLDER>;
   - [GitHub Copilot Prompt Engineering](https://docs.github.<REDACTED_BLOB>-engineering)
   - When performing a code review, apply these prompt engineering principles from the [GitHub Copilot documentation](https://docs.github.<REDACTED_BLOB>-engineering)

5. convert-cassandra-to-spring-data-cosmos.instructions.md (lines 121, 1011)
   - [Microsoft.<REDACTED_BLOB>] on any scope.
   - to perform action [Microsoft.<REDACTED_BLOB>]

6. dataverse-python-advanced-features.instructions.md (line 725)
   - [Official Walkthrough Example](https://github.com/microsoft/PowerPlatform-DataverseClient-<REDACTED_BLOB>.py)

7. dataverse-python-agentic-workflows.instructions.md (line 367)
   - self.llm = OpenAI(api_key: <REDACTED_PLACEHOLDER>)

8. dataverse-python-authentication-security.instructions.md (multiple lines)
   - client_secret: <REDACTED_PLACEHOLDER>["AZURE_CLIENT_SECRET"] (x3 occurrences)
   - AZURE_CLIENT_SECRET: <REDACTED_PLACEHOLDER>
   - secret: <REDACTED_PLACEHOLDER>("dataverse-client-secret")
   - [Authenticate to Azure Services](https://learn.microsoft.com/en-<REDACTED_BLOB>)

9. dataverse-python-error-handling.instructions.md (line 537)
   - [Azure SDK Error Handling](https://learn.microsoft.com/en-<REDACTED_BLOB>)

10. dataverse-python-real-world-usecases.instructions.md (line 290)
    - self.api_key: <REDACTED_PLACEHOLDER>

11. dotnet-maui.instructions.md (line 34)
    - NEVER place ScrollView or CollectionView inside <REDACTED_BLOB> (can break scrolling and virtualization). Use Grid as the parent layout.

12. joyride-user-project.instructions.md (multiple lines)
    - multiple host URLs with <REDACTED_BLOB> placeholders in links and docs references

13. moodle.instructions.md (line 19)
    - Follow the official Moodle Coding guidelines: <https://moodledev.<REDACTED_BLOB>>

14. pcf-events.instructions.md (line 57)
    - addEventHandler method reference: learn.microsoft.com/en-us/power-apps/developer/model-driven-<REDACTED_BLOB>

15. pcf-power-pages.instructions.md (lines 56-57)
    - Device.getBarcodeValue / Device.getCurrentPosition docs references with <REDACTED_BLOB>

16. power-bi-devops-alm-best-practices.instructions.md (line 380)
    - $servicePrincipalSecret: <REDACTED_PLACEHOLDER> -VaultName $KeyVaultName -Name "PowerBI-ServicePrincipal-Secret-$Environment" -AsPlainText

17. security-and-owasp.instructions.md (line 28)
    - const apiKey: <REDACTED_PLACEHOLDER>;

18. springboot-4-migration.instructions.md (line 625)
    - Review [Spring Boot commit ...](https://github.com/spring-projects/spring-<REDACTED_BLOB>)

19. typescript-mcp-server.instructions.md (multiple lines)
    - imports and package names redacted: '@<REDACTED_BLOB>.js' (x4 occurrences)

---

Next steps recommended:

1. Human reviewers: open `artifacts/instructions_auto_fixes.zip` and inspect these files; replace placeholders where appropriate and confirm final wording.
2. After approval, update files in `docs/instructions/` with approved text and re-run the validator: `python tools/validate_instructions_frontmatter.py`.
3. Merge `chore/instructions-auto-fix` after CI green (workflow: `.github/workflows/instructions-validate.yml`).

If you want, proceed now to commit the imported files and artifacts and open/update PR #11 with these additions.
