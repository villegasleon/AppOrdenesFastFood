import React from 'react';
import Order from './Order';

class OrdersTab extends React.Component {
    // Constructor 
    constructor(props) {
        super(props);
        this.reloadFn = this.reloadFn.bind(this);
        this.state = {
            items: [],
            DataisLoaded: false
        };
    }

    componentDidMount() {
        fetch(
            "http://127.0.0.1:5000/orders?status="+this.props.status)
                    .then((res) => res.json())
                    .then((json) => {
                        console.log(this.props.status);
                        console.log(json);
                        this.setState({
                            items: json.data,
                            DataisLoaded: true
                        });
                    })
    }

    reloadFn(){
        this.componentDidMount();
    }

  render() {    

    const { DataisLoaded, items } = this.state;

    if (!DataisLoaded) return <div>
        <h1> Please wait.... </h1> </div> ;

        
    if (items.length==0) return <div>
        <h4> There's no orders with status {this.props.status} </h4> </div> ;

      return (
      <div className="OrdersTab">
        
        {
        
        items.map((item) => ( 
            <div>
                <div className='container'>
                        <div className="row">
                            <div className="col-7 justify-content-start">
            <Order reloadFn={this.reloadFn} orderId={item.OrdersId} itemsProducts={item.items} status={this.props.status} nextStatus={this.props.nextStatus}></Order>
</div>
                        </div>
                            <div className="col-7"></div>
                </div>
            <br></br>
            </div>
        ))
    }
      </div>
    );
  }
};

export default OrdersTab;