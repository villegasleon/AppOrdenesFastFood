import React from 'react';

class Order extends React.Component {
    constructor(props) {
        super(props);
    }

    sendNextStatus(e,nextStatus){
        const requestOptions = {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ status: nextStatus })
        };
        fetch(
            "http://127.0.0.1:5000/orders/"+this.props.orderId,requestOptions)
                    .then((res) =>{
                        res.json();
                        this.props.reloadFn();
                    } );
    };

  render() {
    let button;
    let cancelButton;
        if(this.props.nextStatus==''){
            button='';
            cancelButton='';                                        
        }
        else{
        button = <button className='btn btn-success' onClick={event => this.sendNextStatus(event, this.props.nextStatus)}>{this.props.nextStatus}</button>
        cancelButton = <button className='btn btn-danger' onClick={event => this.sendNextStatus(event, 'Canceled')}>Cancel</button>;
        }
      
        return (
      <div className="Order">
        <div className="card">
            <div className="card-body">
                <div className="card-title">
                    <div className='container'>
                        <div className='row'>
                            <div className='col-8'>
                                
                                <h5>Order #{this.props.orderId}</h5>
                            </div>
                            <div className='col-4'>
                                <h5>{this.props.status}</h5>
                            </div>
                        </div>
                    </div>
                </div>

                <div className="card-body">

                    <div className="container">
                        <div className="row">
                            <div className="col-8 g-0">
                                <b>Products</b>
                                {
                                    this.props.itemsProducts.map((item) => (
                                        <div> 
                                            {item.ProductName} - {item.Amount}
                                        </div>
                                    ))
                                }
                            </div>
                            <div className="col-4 ms-auto">
                                {button}
                            </div>
                        </div>
                        <div className="row">
                            
                        <div className="col-8"></div>
                            <div className="col-4 ms-auto">
                                {cancelButton}
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>

      </div>
    );
  }
}

export default Order;