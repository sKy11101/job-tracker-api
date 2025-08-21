import { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const API = "http://localhost:5000"; // adjust to your backend
  const [form, setForm] = useState({ title: "", company: "", platform: "", job_url: "" });
  const [jobs, setJobs] = useState([]);

  const load = async () => {
    const res = await axios.get(`${API}/jobs`);
    setJobs(res.data);
  };

  useEffect(() => {
    load();
  }, []);

  const submit = async (e) => {
    e.preventDefault();
    if (!form.title || !form.company) return alert("Title & Company required");
    await axios.post(`${API}/jobs`, form);
    setForm({ title: "", company: "", platform: "", job_url: "" });
    load();
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6 flex flex-col items-center">
      <h1 className="text-3xl font-bold text-gray-800 mb-8">
        Job Tracker <span className="text-indigo-600">(MVP)</span>
      </h1>

      {/* Form */}
      <form
        onSubmit={submit}
        className="bg-white p-6 rounded-2xl shadow-lg w-full max-w-4xl grid gap-4 md:grid-cols-4"
      >
        <input
          className="border border-gray-300 p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
          placeholder="Job Title"
          value={form.title}
          onChange={(e) => setForm({ ...form, title: e.target.value })}
        />
        <input
          className="border border-gray-300 p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
          placeholder="Company"
          value={form.company}
          onChange={(e) => setForm({ ...form, company: e.target.value })}
        />
        <input
          className="border border-gray-300 p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
          placeholder="Platform (e.g., LinkedIn)"
          value={form.platform}
          onChange={(e) => setForm({ ...form, platform: e.target.value })}
        />
        <input
          className="border border-gray-300 p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
          placeholder="Job URL"
          value={form.job_url}
          onChange={(e) => setForm({ ...form, job_url: e.target.value })}
        />

        <button
          className="md:col-span-4 bg-indigo-600 text-white font-semibold py-3 rounded-lg hover:bg-indigo-700 transition"
        >
          ➕ Add Job
        </button>
      </form>

      {/* Jobs List */}
      <div className="w-full max-w-4xl mt-8 space-y-4">
        {jobs.length === 0 ? (
          <div className="text-gray-500 text-center">No jobs added yet.</div>
        ) : (
          jobs.map((j) => (
            <div
              key={j.job_id}
              className="bg-white p-5 rounded-2xl shadow flex justify-between items-center hover:shadow-md transition"
            >
              <div>
                <div className="font-semibold text-lg text-gray-800">{j.title}</div>
                <div className="text-sm text-gray-600">
                  {j.company} · {j.platform || "—"}
                </div>
              </div>
              <a
                href={j.job_url}
                target="_blank"
                rel="noopener noreferrer"
                className="text-indigo-600 font-medium hover:underline"
              >
                Open
              </a>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default App;

