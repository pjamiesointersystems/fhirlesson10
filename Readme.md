# FHIR Lesson 10: Bundles and Batch Operations

Welcome to Lesson 10 of the InterSystems IRIS for Health FHIR Developer Curriculum. This module introduces students to the advanced mechanics of **FHIR Bundles**, including **batch**, **transaction**, **history**, **collection**, **document**, and **message** types. Through both conceptual explanation and practical exercises, students will build and manipulate FHIR Bundles using real-world healthcare data scenarios.

---

## 🎯 Learning Objectives

By the end of this lesson, students will be able to:

- Differentiate between the types of FHIR Bundles and their intended uses.
- Construct and send **batch** and **transaction** bundles for multi-operation FHIR processing.
- Create **collection** and **document** bundles for packaging related resources.
- Generate **UUID-based fullUrls** and apply `urn:uuid:` schemes in transaction bundles.
- Use history bundles to audit resource versioning and trace changes.
- Understand when to use **message bundles** for event-driven communication.

---

## 📁 Repository Contents
lesson-10/
├── README.md # This file
├── FHIR Bundle and Batch Operations Final.pptx # Instructional slides
├── fhirbatchbundlewithPatch.http # Example bundle: PATCH within batch
├── fhirbatchdelete.http # Example: DELETE operations in batch
├── fhirtranspatchbundle.http # Transaction + PATCH bundle
├── fhirhistorybundle.http # Bundle for historical resource states
├── fhirsurgerytransactionbatch.http # Simulated transaction for surgery case
├── uuidgen.py # Python tool for UUID generation
├── base64encode.py # Script for encoding FHIR auth headers

## 🔧 Key Bundle Types Explored

| Bundle Type   | Description |
|---------------|-------------|
| `collection`  | A list of resources grouped together, but not processed |
| `batch`       | Executes independent requests (e.g., mix of GET, POST, DELETE) |
| `transaction` | All-or-nothing request block—atomic execution |
| `history`     | Returns prior versions of a resource |
| `message`     | Used for event-based FHIR communications |
| `document`    | A clinical document with a Composition and supporting entries |

---

## 🧪 Example Use Cases

- **Batch Processing:** Send multiple unrelated requests (e.g., GET a patient, POST a new observation).
- **Transaction Bundles:** Simultaneously create a `Patient`, `Encounter`, and `Observation` atomically.
- **History Retrieval:** Retrieve all versions of a resource for auditing.
- **FHIR Document Assembly:** Create a discharge summary with a `Composition` and associated `Patient` and `Observation`.

---

## 🛠 Running the Examples

### Requirements:
- A FHIR server that supports batch and transaction operations (e.g., InterSystems IRIS for Health or HAPI FHIR).
- `curl`, Postman, or a REST client.
- Python 3 for running `uuidgen.py` and `base64encode.py`.

### Running the UUID Generator:
```bash
python uuidgen.py
Use the output to populate fullUrl fields in transaction bundles (urn:uuid:<your-guid>).


🧠 Key Lessons
Use POST [base] to submit both batch and transaction bundles.

Only transaction bundles enforce atomicity—fail one, fail all.

Use fullUrl with urn:uuid: in transactions to link references internally.

Batch requests return individual status per entry—some may fail.

Historical versions are immutable; FHIR does not allow deleting specific versions.

👩‍⚕️ Clinical Framing
The lesson simulates complex workflows like surgical scheduling and home care discharge using bundle-based interactions. These real-world examples mirror what healthcare organizations need to automate system integrations, batch updates, and reliable transactions using FHIR standards.

✍️ Credits
Created by:

Patrick W. Jamieson, M.D., Technical Product Manager

Russ Leftwich, M.D., Senior Clinical Advisor for Interoperability

Part of the official InterSystems FHIR educational series.

---




