% include('layouts/header.tpl', title='HomePage')

<div class="jumbotron">
  <div class="container-fluid">
    <h1 class="display-3">Crypto Rates</h1>
      <table class="table table-hover table-bordered">
        <thead>
          <tr>
            <th>Name</th>
            <th>Code</th>
            <th>Trend</th>
            <th>Rate</th>
          </tr>
        </thead>
        <tbody>
          %for row in rows:
            <tr>
            %for col in row:
              <td>{{col}}</td>
            %end
            </tr>
          %end
        </tbody>
      </table>
  </div>
</div>

% include('layouts/footer.tpl')
