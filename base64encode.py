import base64

def to_base64(input_string):
    # Convert string to bytes
    bytes_data = input_string.encode('utf-8')
    # Encode to Base64
    base64_bytes = base64.b64encode(bytes_data)
    # Convert back to string
    return base64_bytes.decode('utf-8')

# Example input
json_patch = '''
[{
  "op": "replace",
  "path": "/gender",
  "value": "female"
}]
'''

# Apply the function
encoded_patch = to_base64(json_patch)
print(encoded_patch)

""" FHIR Bundles Require resource to Be a FHIR Resource
In a transaction or batch Bundle:

The entry.resource field must contain a valid FHIR resource (e.g., Patient, Observation, Binary, etc.).
JSON Patch documents (arrays of operations) are not valid FHIR resources — they are just raw JSON.
💡 So you can't directly insert a JSON Patch array into entry.resource. That would violate the FHIR schema, and servers would reject it.
2. The Binary Resource is Designed for Raw Data
FHIR defines Binary as a wrapper for arbitrary binary content (like PDFs, images, or JSON blobs).

It includes:
contentType – specifying the MIME type (e.g., application/json-patch+json)
data – Base64-encoded content
🔐 This allows you to embed any arbitrary payload (including JSON Patch) inside a valid FHIR resource, which makes it acceptable inside a bundle.

✅ 3. PATCH + Binary Enables Transactional Updates
The trick is this:

You create a Binary resource that contains a base64-encoded JSON Patch document.
You then PATCH a target resource (e.g., Patient/1), using that Binary as the body. """