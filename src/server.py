import json
import asyncio
from mcp.server import Server
from mcp.types import Tool, TextContent
from typing import Any, Dict, List

# Mock job data for MVP
MOCK_JOBS = [
    {
        "id": "job_1",
        "title": "Senior Python Developer",
        "company": "TechCorp UK",
        "location": "London",
        "salary": "£70,000 - £90,000",
        "type": "Full-time",
        "posted": "2024-01-15",
        "description": "Senior Python developer role with AWS experience required."
    },
    {
        "id": "job_2", 
        "title": "DevOps Engineer",
        "company": "CloudStart",
        "location": "Manchester",
        "salary": "£55,000 - £75,000",
        "type": "Full-time",
        "posted": "2024-01-14",
        "description": "DevOps engineer with Kubernetes and AWS expertise."
    },
    {
        "id": "job_3",
        "title": "Data Scientist",
        "company": "DataFlow Ltd",
        "location": "Edinburgh",
        "salary": "£60,000 - £80,000",
        "type": "Full-time",
        "posted": "2024-01-13",
        "description": "Data scientist role focusing on machine learning and analytics."
    }
]

app = Server("jobsearch-mcp-aws")

@app.list_tools()
async def list_tools() -> List[Tool]:
    return [
        Tool(
            name="search_jobs",
            description="Search for jobs in the UK by keywords and location",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Job search keywords (e.g., 'python developer')"
                    },
                    "location": {
                        "type": "string", 
                        "description": "UK location (e.g., 'London', 'Manchester')"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of jobs to return",
                        "default": 10
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="get_job_details",
            description="Get detailed information about a specific job",
            inputSchema={
                "type": "object",
                "properties": {
                    "job_id": {
                        "type": "string",
                        "description": "Unique job identifier"
                    }
                },
                "required": ["job_id"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
    if name == "search_jobs":
        return await search_jobs(arguments)
    elif name == "get_job_details":
        return await get_job_details(arguments)
    else:
        raise ValueError(f"Unknown tool: {name}")

async def search_jobs(args: Dict[str, Any]) -> List[TextContent]:
    query = args.get("query", "").lower()
    location = args.get("location", "").lower()
    limit = args.get("limit", 10)
    
    # Simple filtering logic for MVP
    filtered_jobs = []
    for job in MOCK_JOBS:
        if query in job["title"].lower() or query in job["description"].lower():
            if not location or location in job["location"].lower():
                filtered_jobs.append(job)
    
    # Limit results
    filtered_jobs = filtered_jobs[:limit]
    
    if not filtered_jobs:
        return [TextContent(
            type="text",
            text="No jobs found matching your criteria."
        )]
    
    # Format results
    result_text = f"Found {len(filtered_jobs)} job(s):\n\n"
    for job in filtered_jobs:
        result_text += f"**{job['title']}** at {job['company']}\n"
        result_text += f"📍 {job['location']} | 💰 {job['salary']} | 📅 {job['posted']}\n"
        result_text += f"ID: {job['id']}\n\n"
    
    return [TextContent(type="text", text=result_text)]

async def get_job_details(args: Dict[str, Any]) -> List[TextContent]:
    job_id = args.get("job_id")
    
    # Find job by ID
    job = next((j for j in MOCK_JOBS if j["id"] == job_id), None)
    
    if not job:
        return [TextContent(
            type="text",
            text=f"Job with ID '{job_id}' not found."
        )]
    
    # Format detailed job info
    details = f"""**{job['title']}**
Company: {job['company']}
Location: {job['location']}
Salary: {job['salary']}
Type: {job['type']}
Posted: {job['posted']}

**Description:**
{job['description']}

**Job ID:** {job['id']}
"""
    
    return [TextContent(type="text", text=details)]

# Lambda handler
def lambda_handler(event, context):
    """AWS Lambda handler for MCP server"""
    try:
        # Run the MCP server
        asyncio.run(app.run())
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'MCP server executed successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }