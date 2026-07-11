function InteractionForm({ interaction }) {
  return (
    <div>
      <h2>Interaction Details</h2>

      <label>HCP Name</label>
      <input
        type="text"
        value={interaction.hcpName}
        readOnly
      />

      <label>Date</label>
      <input
        type="text"
        value={interaction.date}
        readOnly
      />

      <label>Product</label>
      <input
        type="text"
        value={interaction.product}
        readOnly
      />

      <label>Sentiment</label>
      <input
        type="text"
        value={interaction.sentiment}
        readOnly
      />

      <div className="checkbox">
        <input
          type="checkbox"
          checked={interaction.brochure}
          readOnly
        />
        <label>Brochure Shared</label>
      </div>

      <div className="checkbox">
        <input
          type="checkbox"
          checked={interaction.followup}
          readOnly
        />
        <label>Follow-up Required</label>
      </div>

      <label>Summary</label>
      <textarea
        rows="6"
        value={interaction.summary}
        readOnly
      />
    </div>
  );
}

export default InteractionForm;