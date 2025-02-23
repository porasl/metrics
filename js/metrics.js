import React from 'react';
import { Bar, Doughnut } from 'react-chartjs-2';

const Dashboard = () => {
  // Sample data for charts (replace with your data)
  const orderPerMinData = {
    labels: ['10:00', '10:01', '10:02', '10:03', '10:04', '10:05'],
    datasets: [{
      label: 'Orders Per Min',
      data: [12, 19, 3, 5, 2, 3],
      backgroundColor: 'rgba(75, 192, 192, 0.6)',
    }]
  };

  const orderPerHourData = {
    labels: ['10 AM', '11 AM', '12 PM', '1 PM', '2 PM', '3 PM'],
    datasets: [{
      label: 'Orders Per Hour',
      data: [200, 300, 250, 400, 450, 500],
      backgroundColor: 'rgba(54, 162, 235, 0.6)',
    }]
  };

  const paymentTypesData = {
    labels: ['Credit Card', 'PayPal', 'Cash', 'Other'],
    datasets: [{
      data: [200, 150, 100, 50],
      backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0'],
    }]
  };

  return (
    <div className="dashboard">
      <div className="header">
        <div className="date-time">
          <label>Select date / time:</label>
          <input type="datetime-local" defaultValue="2025-01-28T10:00" />
        </div>
        <button>Start</button>
      </div>

      <div className="main-stats">
        <div className="revenue">
          <label>Revenue USD</label>
          <h2>$543,226</h2>
        </div>
        <div className="orders">
          <label>Number of Orders</label>
          <h2>2,487</h2>
        </div>
      </div>

      <div className="order-status">
        <h3>Orders Status</h3>
        <p>Completed: 4353</p>
        <p>Returned: 43</p>
        <p>Submitted to fulfillment: 234</p>
        <p>Received by fulfillment: 234</p>
        <p>Canceled: 11</p>
        <p>Ready to Pickup: 2</p>
        <p>Payment Review: 4</p>
      </div>

      <div className="inventory">
        <h3>Inventory</h3>
        <table>
          <thead>
            <tr>
              <th>SKU Id</th>
              <th>QTY</th>
              <th>Backordered</th>
              <th>Updated Time</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>014334534</td>
              <td>1453</td>
              <td>0</td>
              <td>28/01/2025 03:44:33 PM</td>
            </tr>
            <tr>
              <td>012354754</td>
              <td>923</td>
              <td>0</td>
              <td>28/01/2025 03:23:54 PM</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div className="charts">
        <div className="chart">
          <h4>Order Per Min</h4>
          <Bar data={orderPerMinData} />
        </div>
        <div className="chart">
          <h4>Orders Per Hour</h4>
          <Bar data={orderPerHourData} />
        </div>
        <div className="chart">
          <h4>Payment Types</h4>
          <Doughnut data={paymentTypesData} />
        </div>
      </div>

      <div className="download">
        <a href="#">Order Details: Download</a>
      </div>
    </div>
  );
};

export default Dashboard;
