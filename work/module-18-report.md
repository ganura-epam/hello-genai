# Module 18 Completion Report

## Target Application
- URL: https://github.com/ganura-epam/hello-genai

## QA Findings
| # | Category | Finding | Severity | MCP Tool Used |
|---|----------|---------|----------|---------------|
| 1 | Performance | Time to First Byte (TTFB) is 611ms — above the recommended 200ms threshold for a good user experience | Medium | browser_evaluate |
| 2 | Accessibility | 7 out of 24 buttons have no `aria-label` and no visible text content, making them undiscoverable to screen readers | High | browser_evaluate |
| 3 | Performance | 1 slow resource (`collect`) took 1232ms to load — above the 1000ms slow-resource threshold | Medium | browser_evaluate |
| 4 | Performance | Page loaded 146 resources with a total transfer size of 39,590 bytes on initial load | Low | browser_evaluate |
| 5 | Network | 141 static asset requests were made on page load (JS, CSS, images) — indicates no aggressive resource bundling | Low | browser_network_requests |

## MCP Tools Used
- browser_navigate
- browser_console_messages
- browser_network_requests
- browser_evaluate
